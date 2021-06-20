import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#resetarea pinilor
GPIO.cleanup()

#setarea pinului ce imi va da viteza motorului
motor_speed_pin = 8
#setarea pinilor de directie
DIRA = 10
DIRB = 22

#setarea pinilor de output
GPIO.setup(motor_speed_pin, GPIO.OUT)
GPIO.setup(DIRA, GPIO.OUT)
GPIO.setup(DIRB, GPIO.OUT)

#stingerea ledului rosu
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,1)

#aprinderea ledului verde
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,0)

pwmPin = GPIO.PWM(motor_speed_pin, 80)

GPIO.output(DIRA, GPIO.LOW)
GPIO.output(DIRB, GPIO.LOW)

#oprirea motorului
pwmPin.stop()
