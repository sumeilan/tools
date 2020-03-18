#encoding:utf-8
import os
import time
import csv

#App类
#触漫:adb shell am start -W -n com.mallestudio.gugu.app/com.mallestudio.gugu.modules.StartActivity
#柠檬精：adb shell am start -W -n com.mallestudio.flash/.ui.splash.LauncherActivity
class App(object):
    def __init__(self):
        self.content = ""
        self.startTime=""
    #启动App
    def LaunchApp(self):
        cmd = "adb shell am start -W -n com.mallestudio.flash/.ui.splash.LauncherActivity"
        # cmd = "adb shell am start -W -n com.mallestudio.gugu.app/com.mallestudio.gugu.modules.StartActivity"
        self.content = os.popen(cmd)

    #停止App
    def StopApp(self):
        cmd = "adb shell am force-stop com.mallestudio.flash"
        # cmd = "adb shell am force-stop com.mallestudio.gugu.app"
        os.popen(cmd)
    #获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime

#控制类
class Controller(object):
    def __init__(self,count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp","elapsedtime")]

    #单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(5)
        elapsedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        currenttime = self.getCurrentTime()
        time.sleep(3)
        self.alldata.append((currenttime,elapsedtime))

    #多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1

    #获取执行的当前时间
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = open("startTime.csv","w")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSV()