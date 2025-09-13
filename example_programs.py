from pybricks.parameters import Button, Stop
from robot import hub, drive_base, left_drive, right_drive
from pybricks.tools import wait, run_task, multitask

def drive_forever():
    drive_base.drive(100,0)
    wait(250)
    while not Button.CENTER in hub.buttons.pressed():
        wait(25)
    drive_base.stop()
    wait(250)


def turn_left():
    drive_base.turn(-90, Stop.COAST_SMART)

def turn_right():
    drive_base.turn(90, Stop.COAST_SMART)
