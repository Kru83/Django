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

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D django
RUN chown -R django:django /vol

RUN chmod -R 755 /vol/web
USER django

CMD ["entrypoint.sh"]
