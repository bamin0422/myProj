#########################################################################
### Date: 2017/10/13
### file name: trackingModule.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction
###
#########################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep
from swingTurnModule import rightSwingTurn
from swingTurnModule import leftSwingTurn
from ultraModule import getDistance
from pointTurnModule import rightPointTurn
from pointTurnModule import leftPointTurn
from go_any import go_forward_any
from go_any import go_backward_any
from go_any import go_forward
from go_any import go_backward
from go_any import stop
from go_any import LeftPwm
from go_any import RightPwm
from go_any import pwm_setup
from go_any import pwm_low



# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

# =======================================================================
# declare the pins of 16, 18, 22, 40, 32 in the Rapberry Pi
# as the control pins of 5-way trackinmg sensor in order to
# control direction
#
#  leftmostled    leftlessled     centerled     rightlessled     rightmostled
#       16            18              22             40              32
#
# led turns on (1) : trackinmg sensor led detects white playground
# led turns off(0) : trackinmg sensor led detects black line

# leftmostled off : it means that moving object finds black line
#                   at the position of leftmostled
#                   black line locates below the leftmostled of the moving object
#
# leftlessled off : it means that moving object finds black line
#                   at the position of leftlessled
#                   black line locates below the leftlessled of the moving object
#
# centerled off : it means that moving object finds black line
#                   at the position of centerled
#                   black line locates below the centerled of the moving object
#
# rightlessled off : it means that moving object finds black line
#                   at the position of rightlessled
#                   black line locates below the rightlessled  of the moving object
#
# rightmostled off : it means that moving object finds black line
#                   at the position of rightmostled
#                   black line locates below the rightmostled of the moving object
# =======================================================================

leftmostled = 16
leftlessled = 18
centerled = 22
rightlessled = 40
rightmostled = 32

# =======================================================================
# because the connetions between 5-way tracking sensor and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared whether their roles of pins
# are output pin or input pin
# since the 5-way tracking sensor data has been detected and
# used as the input data, leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared as input
#
# =======================================================================

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)

# =======================================================================
# GPIO.input(leftmostled) method gives the data obtained from leftmostled
# leftmostled returns (1) : leftmostled detects white playground
# leftmostled returns (0) : leftmostled detects black line
#
#
# GPIO.input(leftlessled) method gives the data obtained from leftlessled
# leftlessled returns (1) : leftlessled detects white playground
# leftlessled returns (0) : leftlessled detects black line
#
# GPIO.input(centerled) method gives the data obtained from centerled
# centerled returns (1) : centerled detects white playground
# centerled returns (0) : centerled detects black line
#
# GPIO.input(rightlessled) method gives the data obtained from rightlessled
# rightlessled returns (1) : rightlessled detects white playground
# rightlessled returns (0) : rightlessled detects black line
#
# GPIO.input(rightmostled) method gives the data obtained from rightmostled
# rightmostled returns (1) : rightmostled detects white playground
# rightmostled returns (0) : rightmostled detects black line
#
# =======================================================================

data=[
    ['01111', 15, 0],
    ['00111', 15, 3],
    ['00011', 15, 5],
    ['10111', 15, 7],
    ['10011', 15, 9],
    ['11110', 0, 15],
    ['11100', 3, 15],
    ['11000', 5, 15],
    ['11101', 7, 15],
    ['11001', 9, 15],
    ['11011', 15, 15],
    ['10001', 15, 15]
]

def go(left, right):
    LeftPwm.start(left * 2)
    RightPwm.start(right * 2)

def linetracing():

    answer = str(GPIO.input(leftmostled)) + str(GPIO.input(leftlessled)) + str(GPIO.input(centerled)) + str(GPIO.input(rightlessled)) + str(GPIO.input(rightmostled))

    for i in range(len(data)):

        if answer == data[i][0]:
            go(data[i][1], data[i][2])
            sleep(0.5)
            print(answer)
            break
            pass
        pass

dis = 10
SwingPr = 42
SwingTr = 1.0 * 1.47

PointPr = 37
PointTr = 0.8 * 1.9
try:
    while True:

        distance=getDistance()


        if distance > dis:
            linetracing()


        else:
            stop()
            sleep(1)
            go(0, 15)
            sleep(1)
            stop()
            go(15, 7)
            sleep(1)
            stop()

except KeyboardInterrupt:
    GPIO.cleanup()
