import time

import picamera

import picamera.array

import cv2 as CV2



with picamera.PiCamera() as camera:

        camera.start_preview()

        time.sleep(20)

        with picamera.array.PiRGBArray(camera) as stream:

            camera.capture(stream, format='rgb')#format类型：bgr\rgb\h264

        # 此时就可以获取到bgr的数据流了

            image = stream.array



#image_resize = CV2.resize(image,(1920, 1088)) #opencv改变分辨率
image_resize = image

CV2.imshow('IMAGE',image_resize)

CV2.imwrite('output2.png',image_resize)
CV2.imwrite('output2.jpg',image_resize)
CV2.waitKey(0)

CV2.destroyAllWindows()