from django.shortcuts import render

# Create your views here.
def congress(request):
    return render (request, 'congress.html')

#def homepage(request):
#    return render (request, 'index.html')