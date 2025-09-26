from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Port, Direction

hub = PrimeHub()

#Adjust these parameters to fit your robot. Also ensure that you add any sensors here.
#Small basic robot

left_drive = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.E, Direction.CLOCKWISE)

drive = DriveBase(left_drive, right_drive, 56, 96)
drive.use_gyro(True)
