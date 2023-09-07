import cv2
import numpy as np
img = cv2.imread("yuanshi.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(type(img))
out = 1.31*img
print(out)
out[out>255] = 255
out[out<255] = 0
out = np.around(out)
cv2.imwrite("chuli.png", out)
