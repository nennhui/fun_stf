from django.shortcuts import render
import os
# Create your views here.
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

def physical (request):
    """
        获取命令，进行物理操作
    """

    cmd=request.POST.get('cmd')
    os.system("adb shell input keyevent {}", format(Keycode.cmd))


class Keycode():
    home="KEYCODE_HOME"
    menu="KEYCODE_MENU"
    back='KEYCODE_BACK'
    light='224'    #唤起屏幕
    dark='223'     #锁屏