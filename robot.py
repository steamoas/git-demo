from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Port, Direction

hub = PrimeHub()
#Adjust these parameters to fit your robot. Also ensure that you add any sensors here.

left_drive = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.A, Direction.CLOCKWISE)

drive = DriveBase(left_drive, right_drive, 50, 100)
