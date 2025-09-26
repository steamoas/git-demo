from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Port, Direction

hub = PrimeHub()
#Adjust these parameters to fit your robot. Also ensure that you add any sensors here.
#David's Robot

left_drive = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.F, Direction.CLOCKWISE)

drive = DriveBase(left_drive, right_drive, 60, 104)
drive.use_gyro(True)
