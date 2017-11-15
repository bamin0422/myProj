######################################################################
### Date: 2017/10/5
### file name: go_any.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to go forward or backward without time limit
######################################################################

# import GPIO library
import RPi.GPIO as GPIO

from time import sleep

# set GPIO warnings as flase
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)


# =======================================================================
# REVERSE function to control the direction of motor in reverse
# =======================================================================
def REVERSE(x):
    if x == 'True':
        return 'False'
    elif x == 'False':
        return 'True'


# =======================================================================
# Set the motor's true / false value to go forward.
# =======================================================================
forward0 = 'True'
forward1 = 'False'

# =======================================================================
# Set the motor's true / false value to go opposite.
# =======================================================================
backward0 = REVERSE(forward0)
backward1 = REVERSE(forward1)

# =======================================================================
# declare the pins of 12, 11, 35 in the Rapberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Rapberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
# =======================================================================
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================

def leftmotor(x):
    if x == 'True':
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    elif x == 'False':
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    else:
        print
        'Config Error'


def rightmotor(x):
    if x == 'True':
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    elif x == 'False':
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    else:
        print
        'Config Error'


# student assignment (6)

# =======================================================================
# because the connetions between motors (left motor) and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# =======================================================================
# because the connetions between motors (right motor) and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  objec to go forward without any limitation of running_time
# =======================================================================

def go_forward_any(left, right):
    leftmotor(forward0)
    leftmotor(forward1)
    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go fowrard
    rightmotor(forward0)
#    rightmotor(forward1)
    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(left)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(right)
    # set the running time of the left motor to go fowrard



# student assignment (7)

# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  objec to go backward without any limitation of running_time
# =======================================================================

def go_backward_any(speed):
  #  leftmotor(forward1)
    leftmotor(forward0)
    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go fowrard
   # rightmotor(forward1)
    rightmotor(forward0)
    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go fowrard



# student assignment (8)

# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  objec to go forward with the limitation of running_time
# =======================================================================

def go_forward(Left, Right, running_time):
    leftmotor(forward0)
    leftmotor(forward1)
    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go fowrard
    rightmotor(forward0)
#    rightmotor(forward1)
    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(Left)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(Right)
    # set the running time of the left motor to go fowrard
    sleep(running_time)


# student assignment (9)


# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  objec to go backward with the limitation of running_time
# =======================================================================

def go_backward(speed, running_time):
    leftmotor(forward1)
    leftmotor(forward0)
    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go fowrard
    rightmotor(forward1)
    rightmotor(forward0)
    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go fowrard
    sleep(running_time)


# student assignment (10)


# =======================================================================
# define the stop module
# =======================================================================
def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)


def pwm_low():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()

