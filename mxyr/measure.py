#picamera2库仅能在linux环境下安装，windows环境测试不了，文档参考picamera2-manual.pdf
from picamera2 import Picamera2

# 拍照部分，可运行，暂时测试不了，注释掉
"""
picam_1 = Picamera2(0)
picam_2 = Picamera2(1)
config_1 = picam_1.create_still_configuration()
config_2 = picam_1.create_still_configuration()
picam_1.configure(config_1)
picam_2.configure(config_2)
print("初始化摄像头！")
picam_1.start()
picam_2.start()
picam_1.capture_file("cam0.png")
picam_2.capture_file("cam1.png")
print("拍照成功！")
picam_1.stop()
picam_2.stop()
"""

