# Personal Website - Django + Docker + uWSGI + Nginx

This project demonstrates a Dockerized Django web application served through **uWSGI** and **Nginx**, with separate configuration for local development and production deployment.

---

## 🚀 Setup Instructions

### 1. Clone and Install Dependencies
```bash
git clone <repo-url>
cd personalwebsite
docker-compose build
```

### 2. Local Development
Use Django's built-in server without uWSGI or Nginx.

#### Run Locally with Docker
```bash
docker-compose up
```

- Django runs on `localhost:8000`
- Static files are served using `DEBUG=1`

**docker-compose.yml**
```yaml
services:
  personalwebsite:
    build:
      context: .
    ports:
      - "8000:8000"
    volumes:
      - ./personalwebsite:/personalwebsite
    command: sh -c "python manage.py runserver 0.0.0.0:8000"
    environment:
      - DEBUG=1
```

Ensure environment variable `DJANGO_DEBUG=1` is set in your IDE (e.g., PyCharm) if running `manage.py runserver` directly.

### 3. Deployment / Server Testing
Use uWSGI + Nginx stack for simulating production.

#### Run with Production Stack
```bash
docker-compose -f docker-compose-deploy.yml up --build
```

**docker-compose-deploy.yml**
```yaml
services:
  personalwebsite:
    build:
      context: .
    volumes:
      - static_data:/vol/web
    environment:
      - DJANGO_SECRET_KEY=your-secret-key
      - DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,www.kru.dev,kru.dev

  proxy:
    build:
      context: ./proxy
    volumes:
      - static_data:/vol/static
    ports:
      - "8000:8000"
    depends_on:
      - personalwebsite

volumes:
  static_data:
```

---

## 🐳 Dockerfile Overview

**App Dockerfile** (runs Django + uWSGI)
```Dockerfile
FROM python:3.13.3-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /personalwebsite
COPY ./personalwebsite /personalwebsite
WORKDIR /personalwebsite
COPY ./scripts /scripts

RUN chmod +x /scripts/*
RUN mkdir -p /vol/web/media /vol/web/static

RUN adduser -D django
RUN chown -R django:django /vol
RUN chmod -R 755 /vol/web

USER django
CMD ["entrypoint.sh"]
```

**entrypoint.sh**
```bash
#!/bin/sh
set -e

python manage.py collectstatic --noinput
uwsgi --socket :8000 --master --enable-threads --module personalwebsite.wsgi
```

---

## 🌐 Nginx Reverse Proxy Configuration

**default.conf**
```nginx
server {
    listen 8000;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass personalwebsite:8000;
        include /etc/nginx/uwsgi_params;
    }
}
```

**proxy Dockerfile**
```Dockerfile
FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

USER root
RUN mkdir -p /vol/static
RUN chmod 755 /vol/static
USER nginx
```

---

## 🧩 Django Static File Settings

```python
STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'
STATIC_ROOT = '/vol/web/static/'
MEDIA_ROOT = '/vol/web/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

To serve static files in production, ensure:
- `collectstatic` runs in `entrypoint.sh`
- Volume `static_data` is mounted in both services
- Nginx has access to `/vol/static`

---

## ✅ Status
- [x] Local development support
- [x] uWSGI production testing
- [x] Nginx proxy
- [x] Static file handling

---

## 🧪 Testing
```bash
Pre-Prod Testing:
docker-compose -f docker-compose-deploy.yml up --build
curl http://localhost:8000

Dev-Testing
docker-compose -f docker-compose.yml up --build
curl http://localhost:8000

```

---

## 📌 Notes
- Avoid port conflicts on `8000` (used by both Nginx and Django dev server).
- For local development, Nginx is **not** required.
- Set `DJANGO_DEBUG=1` for local static files.

---

Happy coding! 🎉

