import cv2
import numpy as np

cimg = cv2.imread("chuli.png")
img = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 5)
# cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(
    img, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=30, minRadius=65, maxRadius=1000
)


circles = np.uint16(np.around(circles))

print(len(circles))
print(circles)
n = 0
for i in circles[0, :]:
    if n < 9:
        # Draw outer circle (blue)
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)

        # Draw Center (red)
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

        n = n + 1
        name = "test" + str(n) + ".png"
        cv2.imwrite(name, cimg)
        # cv2.imshow(name, cimg)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
