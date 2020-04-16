import win32gui
import win32api
import win32con
import cv2
import numpy as np
from PIL import ImageGrab

# 通过gethwnd获得的关键字
classname = 'Qt5QWindowIcon'
titlename = '夜神模拟器'

hwnd = win32gui.FindWindow(classname, titlename)  # 获取特定句柄对应窗口
win32gui.SetForegroundWindow(hwnd)  # 前置窗口
# left, top, right, bot = win32gui.GetWindowRect(hwnd)  # 返回坐标
pos = win32gui.GetWindowRect(hwnd)
m = win32gui.GetCursorPos()  # 鼠标位置
print(pos, '&', m)


def screenshot(wbox):
    img = ImageGrab.grab(wbox)
    img.save('sc.png')


def locate():
    # 读入图片及长宽
    img = cv2.imread('sc.png')
    template = cv2.imread('enemy.png')
    h, w = template.shape[:2]  # ?

    # 2.模板匹配函数与阈值
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.65

    # 运用numpy处理数据
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # *号表示可选参数
        right_bottom = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img, pt, right_bottom, (0, 0, 255), 2)
    """
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_loc)
    left_top = max_loc
    right_bottom = (left_top[0] + w, left_top[1] + h)
    cv2.rectangle(img, left_top, right_bottom, 255, 2)
    """  # 用以寻找单一物体的代码
    cv2.imshow('img', img)
    cv2.waitKey(0)


def click(pos):
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0], pos[1], 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0], pos[1], 0, 0)


def find_enemy():
    # 读入图片及长宽
    img = cv2.imread('sc.png')
    template = cv2.imread('enemy.png')
    h, w = template.shape[:2]  # ?

    # 2.模板匹配函数
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 3.返回相对坐标
    return max_loc


screenshot(pos)
target = find_enemy()
click((target[0]+pos[0]+50, target[1]+pos[1]+50))

