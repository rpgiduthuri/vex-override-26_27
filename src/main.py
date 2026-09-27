# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       ricky                                                        #
# 	Created:      9/26/2026, 5:28:31 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()

controller = Controller()

left_front = Motor(Ports.PORT1, False)
right_front = Motor(Ports.PORT2, True)
left_back = Motor(Ports.PORT3, False)
right_back = Motor(Ports.PORT4, True)
left_stacked = Motor(Ports.PORT5, False)
right_stacked = Motor(Ports.PORT6, True)

left_drive = MotorGroup([left_front, left_back, left_stacked])
right_drive = MotorGroup([right_front, right_back, right_stacked])

def drive(left_speed, right_speed):
    left_drive.set_velocity(left_speed, PERCENT)
    right_drive.set_velocity(right_speed, PERCENT)

def stop_drive():
    left_drive.stop(COAST)
    right_drive.stop(COAST)

def apply_deadband(speed, deadband):
    if abs(speed) < deadband:
        return 0
    return speed

DRIVE_CURVE = 2.5  # Define the drive curve exponent
def apply_curve(speed):
    sign = 1

    if speed < 0:
        sign = -1

    magnitude = abs(speed)
    curved = (magnitude/100) ** DRIVE_CURVE * 100
    return sign * curved


def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    DEADBAND = 5  # Define the deadband threshold
    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        if abs(left_speed) < DEADBAND:
            left_speed = 0
        if abs(right_speed) < DEADBAND:
            right_speed = 0

        left_speed = apply_curve(left_speed)
        right_speed = apply_curve(right_speed)

        left_speed = apply_deadband(left_speed, DEADBAND)
        right_speed = apply_deadband(right_speed, DEADBAND)

        drive(left_speed, right_speed)

        if left_speed == 0 and right_speed == 0:
            stop_drive()

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()