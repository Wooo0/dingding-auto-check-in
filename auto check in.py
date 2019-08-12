# -*- encoding=utf8 -*-

from time import sleep
from airtest.core.api import *
from airtest.core.android.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 连接手机
dev=connect_device("Android://127.0.0.1:5037/")
devs=device()
# 打开电源
keyevent("POWER")
# 获取第三方APP包名
# print(devs.list_app(third_only=True))
# 打开钉钉
start_app("com.alibaba.android.rimet",activity=None)
# sleep(1)
# 点击工作标签
poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.alibaba.android.rimet:id/bottom_tab").offspring("com.alibaba.android.rimet:id/home_bottom_tab_button_work").offspring("com.alibaba.android.rimet:id/home_bottom_tab_icon").click()
sleep(2)
# 点击考勤打卡
poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.alibaba.android.rimet:id/home_content").offspring("dingapp").child("android.view.View")[1].child("android.view.View")[0].child("android.view.View")[1].child("android.view.View").click()
sleep(3)
# 关闭APP
stop_app("com.alibaba.android.rimet")
# 点击HOME
keyevent("HOME")
# 点击power
keyevent("POWER")


