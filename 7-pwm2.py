# CamJam EduKit 3 - Robotics
# Worksheet 7 - Varying the speed of each motor with PWM
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7
# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 30
DutyCycleB = 30
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0
# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)
# Turn all motors off
def stopmotors():
 pwmMotorAForwards.ChangeDutyCycle(Stop)
 pwmMotorABackwards.ChangeDutyCycle(Stop)
 pwmMotorBForwards.ChangeDutyCycle(Stop)
 pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors forwards
def forwards():
 pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
 pwmMotorABackwards.ChangeDutyCycle(Stop)
 pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
 pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors backwards
def backwards():
 pwmMotorAForwards.ChangeDutyCycle(Stop)
 pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
 pwmMotorBForwards.ChangeDutyCycle(Stop)
 pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
# Turn left
def left():
 pwmMotorAForwards.ChangeDutyCycle(Stop)
 pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
 pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
 pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn Right
def right():
 pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
 pwmMotorABackwards.ChangeDutyCycle(Stop)
 pwmMotorBForwards.ChangeDutyCycle(Stop)
 pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
# Your code to control the robot goes below this line
forwards()
time.sleep(1) # Pause for 1 second
left()
time.sleep(0.5) # Pause for half a second
forwards()
time.sleep(1)
right()
time.sleep(0.5)
backwards()
time.sleep(0.5)
stopmotors()
GPIO.cleanup()
