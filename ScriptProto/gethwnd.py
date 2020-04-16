# 获得句柄用的程序

from win32gui import *
title = set()  # 存放得到的名字


def res(hwnd, unk):
    """第二个参数无意义"""
    # 加入条件筛选掉多余句柄
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        title.add(GetWindowText(hwnd) + " && " + GetClassName(hwnd))


EnumWindows(res, 0)  # 枚举句柄
for t in title:
    print(t)

# 得到 夜神模拟器 && Qt5QWindowIcon

