import time

import picamera

import picamera.array

import CV2



with picamera.PiCamera() as camera:

        camera.start_preview()

        time.sleep(2)

        with picamera.array.PiRGBArray(camera) as stream:

        camera.capture(stream, format='rgb')#format类型：bgr\rgb\h264

        # 此时就可以获取到bgr的数据流了

        image = stream.array

import matplotlib.pyplot as plt


image_resize = CV2.resize(image,(320, 240)) #opencv改变分辨率

plt.imshow(image_resize)