# encoding:utf-8
import os, time, sys
import argparse


# 启动app
def launch(env):
    if str(env) == "demo":
        print('demo')
        cmd = "adb shell am start -W -n com.mallestudio.flash.debug/com.mallestudio.flash.ui.splash.LauncherActivity"

    elif str(env) == "official":
        print('official')
        cmd = "adb shell am start -W -n com.mallestudio.flash/com.mallestudio.flash.ui.splash.LauncherActivity"

    else:
        print("none")
        cmd = ""
    os.popen(cmd)
    return


# 点击
def click():
    cmd = "adb shell input tap 500 800"
    os.popen(cmd)


# 上下浏览
def scan(nums):
    time.sleep(5)
    swipe = "adb shell input swipe 500 800 500 10"
    for i in range(nums):
        time.sleep(2)
        os.popen(swipe)


# 左滑
def nextLeft(nums):
    time.sleep(5)
    click()
    swipe = "adb shell input swipe 500 500 100 500"
    for i in range(nums):
        time.sleep(5)
        os.popen(swipe)


# 右滑
def nextRight(nums):
    time.sleep(5)
    click()
    swipe = "adb shell input swipe 100 500 500 500"
    for i in range(nums):
        time.sleep(5)
        os.popen(swipe)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test for argparse')
    parser.add_argument('--env', '-e', default="other")
    parser.add_argument('--num', '-n', default=1)
    parser.add_argument('--script', '-s')

    args = parser.parse_args()
    if args.script is not None:
        if args.script == 'launch':
            launch(args.env)
        if args.script == 'scan':
            scan(int(args.num))
        if args.script == 'nextLeft':
            nextLeft(int(args.num))
        if args.script == 'nextRight':
            nextRight(int(args.num))
