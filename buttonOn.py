import RPi.GPIO as GPIO

#utilizarea notatiei pinilor dupa cum sunt notati pe placuta
GPIO.setmode(GPIO.BOARD)

#pinul ce reprezinta viteza motorului
motor_speed_pin = 8
#pinii urmatori sunt folositi pentru a controla directia motorului
DIRA = 10
DIRB = 22

#setarea pinilor ca output
GPIO.setup(motor_speed_pin, GPIO.OUT)
GPIO.setup(DIRA, GPIO.OUT)
GPIO.setup(DIRB, GPIO.OUT)

#aprinderea ledului rosu
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,0)

#stingerea ledului verde
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,1)

#activarea mototrului
pwmPin = GPIO.PWM(motor_speed_pin, 80)

#setarea vitezei maxime pentru motor
pwmPin.ChangeDutyCycle(80)

#setarea directiei motorului
GPIO.output(DIRA, GPIO.HIGH)
GPIO.output(DIRB, GPIO.LOW)

#pornirea motorului
pwmPin.start(80)
