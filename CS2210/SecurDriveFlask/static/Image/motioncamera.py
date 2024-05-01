from gpiozero import MotionSensor
from gpiozero import LED
from datetime import datetime
import subprocess
import time

pir = MotionSensor(4)
led = LED(17)

takePicture = True

while takePicture:
        filename = "{0:%m}-{0:%d}-{0:%y}-{0:%H}:{0:%M}:{0:%S}.jpg".format(datetime.now())
        pir.wait_for_motion()
        led.on()
        print("Motion Detected")
        time.sleep(2)
        subprocess.run(["libcamera-jpeg", "-o", filename])
        pir.wait_for_no_motion()
        led.off()
        print("Motion Stopped")
        time.sleep(10)
