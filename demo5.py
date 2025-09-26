from pybricks.parameters import Stop
from robot import drive

drive.settings(straight_speed=350)

drive.curve(1200, -45, then = Stop.COAST_SMART)
drive.curve(200, -135, then = Stop.COAST_SMART)

drive.curve(400, 90, then = Stop.COAST_SMART)
drive.curve(300, 90, then = Stop.COAST_SMART)
drive.curve(250, 90, then = Stop.COAST_SMART)

drive.curve(500, 45, then = Stop.COAST_SMART)
drive.curve(150, 45, then = Stop.COAST_SMART)

drive.curve(350, -90, then = Stop.COAST_SMART)
drive.curve(600, 90, then = Stop.COAST_SMART)
