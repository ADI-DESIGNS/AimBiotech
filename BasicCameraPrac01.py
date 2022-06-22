import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024,768)
    camera.start_preview()
    #time delay for camera to start
    time.sleep(20)
    camera.capture("foo02.jpg")
    