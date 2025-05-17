from django.shortcuts import render
from apps.bookgram.gram import *
# Create your views here.

def llm(request):
    response_text = None
    genre = request.POST.get('genre')
    note = request.POST.get('message')
    if request.method == 'POST' and request.POST.get('form_type') == 'creategram':
        response_text = gramllm(genre, note)
    return render(request, 'bookgram.html', {'response_text': response_text})