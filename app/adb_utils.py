#coding:utf-8
import os


class adb_cmd():
    def __init__(self):
        self.devices=[]


    def get_devices(self):
        cmd="adb devices"
        cmd_respone=os.popen(cmd).readlines()
        print((cmd_respone))

        for  devices in cmd_respone:
            try :
                if devices.split('\t')[1]:
                    self.devices.append(devices.split('\t')[0])
            except:
                pass
        print(self.devices)
    def deivce_Api(self):
        self.get_devices()
        port=1717
        port1=1111
        for device  in self.devices:
            #获取手机android api
            cmd_api='adb -s '+device +' shell getprop ro.build.version.sdk'
            cmd_respone=os.popen(cmd_api).readlines()
            device_api=(cmd_respone[0].split('\n')[0])
            #获取手机内核系统
            cmd_prop="adb -s "+device+" shell getprop ro.product.cpu.abi"
            cmd_respone=os.popen(cmd_prop).readlines()
            device_type=(cmd_respone[0].split('\n')[0])

            #推送minicap文件到手机
            cmd_push_minicap_so="adb -s "+device+" push" +" ./stf/minicap_so/android-"+device_api+ "/"+device_type+"/minicap.so"+" /data/local/tmp"
            cmd_respone = os.popen(cmd_push_minicap_so).readlines()
            cmd_push_minicap = "adb -s " + device + " push" + " ./stf/stf_libs/" + device_type + "/minicap"+" /data/local/tmp"
            cmd_respone = os.popen(cmd_push_minicap).readlines()
            cmd_push_minitouch= "adb -s " + device + " push" + " ./stf/stf_libs/" + device_type + "/minitouch"+" /data/local/tmp"
            cmd_respone = os.popen(cmd_push_minitouch).readlines()
            os.popen("adb shell chmod 777 /data/local/tmp/minicap")
            os.popen("adb shell chmod 777 /data/local/tmp/minicap.so")
            os.popen("adb shell chmod 777 /data/local/tmp/minitouch")


            #开启端口映射
            cmd_cap_forward="adb -s " + device + " forward  tcp:"+str(port) +" localabstract:minicap"
            cmd_touch_forward="adb -s " + device + " forward  tcp:"+str(port1) +" localabstract:minitouch"
            cmd_respone = os.popen(cmd_cap_forward).readlines()
            cmd_respone = os.popen(cmd_touch_forward)
            port+=port
            port1 += port1



            #获取手机分辨率
            cmd_px="adb -s " + device + " shell wm size"
            cmd_respone = os.popen(cmd_px).readlines()[0].split('\n')[0]
            device_px=((cmd_respone).split(":")[1].split('\r')[0].split(' ')[1])
            #运行minicap
            cmd_run_minicap=" adb -s " + device + " shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P %s@%s/0"%(device_px,device_px)
            print("www",cmd_run_minicap)
            cmd_respone=os.popen(cmd_run_minicap)
            cmd_run_minitouch=" adb -s " + device + " shell  /data/local/tmp/minitouch"
            print("www",cmd_run_minitouch)
            os.popen(cmd_run_minitouch)



if __name__=="__main__":
    adb_cmd().deivce_Api()
