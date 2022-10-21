import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

LED = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    num = 0
    while(True):
        time.sleep(1)
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        num +=1
        if(num == 5):
            GPIO.cleanup()
            break
except KeyboardInterrupt:
    GPIO.cleanup()