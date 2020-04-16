import cv2
import numpy as np
import matplotlib.pyplot as plt
icon = cv2.imread("ship.png")
origin = cv2.imread("bilan.png")
h, w = icon.shape[:2]
result = cv2.matchTemplate(origin,icon,cv2.TM_CCORR_NORMED)
threshold = 0.9

loc = np.where(result >= threshold)
for pt in zip(*loc[::-1]):
    right_bottom = (pt[0] + w, pt[1] + h)
    cv2.rectangle(origin, pt, right_bottom, (0, 0, 255), 2)
cv2.resize(origin, (460,800))
cv2.imwrite("result.png", origin)
