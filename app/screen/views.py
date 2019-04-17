from django.shortcuts import render,render_to_response
from django.utils.safestring import mark_safe
# Create your views here.
import json
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

def index(request):

    return render(request,"index.html",{})
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def touch(request):
    x=request.POST.get('x')
    y=request.POST.get('y')
    scale_y=int(19199/724)
    scale_x=int(10799/377)
    print(scale_x)
    from screen import  tests
    mc = tests.minitouch('localhost', 1111)
    mc.click(int(x)*scale_x,int(y)*scale_y)
    return render(request,"index.html",{})