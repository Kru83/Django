from django.shortcuts import render

from apps import congress
from apps.congress.congress import *


# Create your views here.
#def congress(request):
#    return render (request, 'congress.html')

def memberByStateView(request):
    if request.method == 'POST':
        stateCode = request.POST.get('state')
        htmlSelectData = congressMemberByState(stateCode)
        members = congressMemberListByState(htmlSelectData)
        return render(request, "congress.html", {'members': members, 'stateCode': stateCode})
    else:
        return render(request,'congress.html')