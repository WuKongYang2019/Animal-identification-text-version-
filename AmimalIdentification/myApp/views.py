from django.shortcuts import render, render_to_response
import Animal_Identification


# Create your views here.
def index(request):
    key = request.GET.get('q', False)
    if not key:
        result = u'请输入内容'
    else:
        result = Animal_Identification.action(key)
    return render_to_response('main.html', {'result': result})
