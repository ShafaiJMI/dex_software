import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

def proximity(trg,echo):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trg,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.output(trg,True)
    time.sleep(0.00001)
    GPIO.output(trg,False)
    startTime = time.time()
    stopTime = time.time()
    while GPIO.input(echo) == 0:
        startTime = time.time()
    while GPIO.input(echo) == 1:
        stopTime = time.time()
    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300)/2
    return int(distance)

class Lid:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        self.servo1 = kit.servo[0]
    def demo(self):
        self.servo1.angle = 45
        #kit.continious_servo[1].throttle = 1
        time.sleep(1)
        self.servo1.angle = 90
        #kit.conitnious_servo[1].throttle = -1
        time.sleep(4)
        self.servo1.angle = 45
        time.sleep(0.5)
        #servo1.angle = 0
        #kit.continious_servo[1].throttle = 0
        self.servo1.angle = 0
    def open(self):
        self.servo1.angle = 90
        time.sleep(4)
        self.servo1.angle = 45
        time.sleep(0.5)
        self.servo1.angle = 90

if __name__ == '__main__':
    try:
        print("Setup Running")
        while True:
            dis = proximity(18,24)
            #print(dis)
            if dis <= 30:
                Lid.open()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Setup Stopped")
        GPIO.cleanup()


