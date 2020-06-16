# encoding:utf-8
import os
import time
import csv

# 柠檬精：adb shell am start -W -n com.mallestudio.flash/.ui.splash.LauncherActivity
def LaunchApp():
    cmd = "adb shell am start -W -n com.mallestudio.flash.debug/.ui.splash.LauncherActivity"
    os.popen(cmd)


def click():
    cmd = "adb shell input tap 500 800"
    os.popen(cmd)

# 上下浏览
def scan(nums):
    LaunchApp()
    time.sleep(6)
    swipe = "adb shell input swipe 500 1000 500 10"
    for i in range(nums):
        time.sleep(2)
        os.popen(swipe)

# 左滑
def next(nums):
    LaunchApp()
    time.sleep(6)
    click()
    swipe1 = "adb shell input swipe 500 500 100 500"
    for i in range(nums):
        # scan(2)
        time.sleep(5)
        os.popen(swipe1)

# 停止App
def StopApp():
    cmd = "adb shell am force-stop com.mallestudio.flash"
    os.popen(cmd)


if __name__ == "__main__":
    option,nums = input("滑动-1，左滑切内容-2，请选择操作和执行的次数:").split()
    if option == "1":
        scan(int(nums))
    else:
        next(int(nums))