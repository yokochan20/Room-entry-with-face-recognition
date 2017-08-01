import wiringpi2
import time
import sys

servopin = 18


def unlock():
	print "Unlock Key"
	param = sys.argv
	setdegree = int(90)
	print setdegree

	wiringpi2.wiringPiSetupGpio()
	wiringpi2.pinMode(servopin,2)
	wiringpi2.pwmSetMode(wiringpi2.GPIO.PWM_MODE_MS)
	wiringpi2.pwmSetClock(375)

	wiringpi2.pwmWrite(servopin,133)
	for i in range(133,73-1,1):
	  print i
	  wiringpi2.pwmWrite(servopin, i)
	  wiringpi2.delay(500)
	
	

	wiringpi2.pwmWrite(servopin,26)
	wiringpi2.delay(500)
	wiringpi2.pwmWrite(servopin,74)

#unlock()
