from ubidots import ApiClient
import Rpi.GPIO as GPIO
import time
import picamera
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

api=ApiClient("2355dc90c5e93fc697295b33f9a6ed4e5003c2e1")

#create a "Variable" object

test_variable=api.get_variable("566993407625420e4e82690a")

while True:
	i=GPIO.input(11)
	i=0
	if i==1
		test_variable.save_value({'value':1})
		camera=picamera.PiCamera()
		camera.capture('suyash.jpg')

		camera.start_preview()
		camera.vflip=True
		camera.hflip=True
		camera.brightness=60
		
		sleep(10)

		i==0