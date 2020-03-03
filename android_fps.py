#encoding:utf-8
import os
import time
import csv

#App类

class App(object):
    def __init__(self):
        self.content = ""
        self.startTime=""
    #启动App
    def LaunchApp(self):
        # cmd = "adb shell am start -W -n com.mallestudio.flash/.ui.splash.LauncherActivity"
        laynchapp = "adb shell am start -W -n com.mallestudio.flash/.ui.splash.LauncherActivity"
        time.sleep(2)
        os.popen(laynchapp)
        swipe = "adb shell input swipe 500 800 500 10"
        for i in range(2):
            time.sleep(1)
            os.popen(swipe)
        cmd = "adb shell dumpsys gfxinfo com.mallestudio.flash > E:/python/tools/fps.txt"
        self.content = os.popen(cmd)

    def control_datas(self):
        #待补充
        pass

app = App()
app.LaunchApp()

