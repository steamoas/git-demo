from pybricks.hubs import PrimeHub
from robot import drive
from robot import hub
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait, run_task

from umath import pi, sqrt

#configure args at the bottom of the file

def track_movement(drive_base: DriveBase, hub: PrimeHub, drive_base_name: str = "drive_base", rounding_digits: int = 1, stop_type: Stop = Stop.HOLD):
    """
    Allows you to track the drive base's movement changes when manually moving your robot. Can also generate python code to replicate these movements using the same drive base.

   Args:
      drive_base (DriveBase): The drive base that you want to use when tracking movement.
      hub (PrimeHub): An instance of your robot's hub. Required for interfacing with buttons.
      drive_base_name (str): The name of the drive base that you want the code generator to use. Defaults to "drive_base".
      rounding_digits (int): The amount of decimal precision you want when generating turning instructions. Defaults to 1.
      stop_type (Stop): The stopping instruction you want to use for generated python code. Defaults to Stop.HOLD.
    """
    hub.light.on(Color.GREEN)
    hub.system.set_stop_button((Button.LEFT, Button.RIGHT))
    drive_base.use_gyro(True)
    print("Welcome to the movement tracking program!")

    print("\nCurrently, the program is in \"single\" mode. It will only count a straight or a turn, not both.")
    print("To enter \"curve\" mode, press the left arrow button. You will notice a 'C' being displayed on the hub.")
    print(f"In \"curve\" mode, each action will give you both a radius and an angle. These can be directly used in the {drive_base_name}.curve() function.")
    print("To re-enter \"straight\" mode, press the right arrow button. You will notice an 'S' being displayed on the hub.")

    print("\nTo begin tracking, press your hub's center button.")
    print("When you want to finish tracking, press the button again. Your movements will be recorded to the console.")
    print("To generate python instructions for your tracked movements, press the bluetooth button.")
    print("To exit, press the left and right arrow buttons simultaneously")

    actions = []
    actions_count = 0
    mode = "straight"
    hub.display.char("S")

    while True:
        buttons = hub.buttons.pressed()
        if Button.CENTER in buttons:

            hub.light.on(Color.RED)
            drive_base.reset()
            drive_base.stop()
            wait(250)

            while not Button.CENTER in hub.buttons.pressed():
                wait(100)

            end_angle = drive_base.angle()
            end_distance = drive_base.distance()

            if mode == "straight":
                if abs(end_angle * 10) > abs(end_distance):
                    actions.append((0, end_angle))
                    print(f"{actions_count}: turn {end_angle} degrees")
                else:
                    actions.append((1, end_distance))
                    print(f"{actions_count}: drive {end_distance} mm")

            elif mode == "curve":
                circumference = end_distance * (360 / end_angle)
                radius = sqrt(circumference/pi)
                actions.append((2, radius, end_distance))
                print(f"{actions_count}: curve with a radius of {radius} of {end_angle} degrees")

            actions_count += 1
            hub.light.on(Color.GREEN)
            wait(250)


        elif Button.BLUETOOTH in buttons:
            print("Generating python code:\n")
            suffix = f", then = {stop_type}" if stop_type != Stop.HOLD else ""
            for i in range(actions_count):
                if actions[i][0] == 0:
                    print(f"{drive_base_name}.turn({round(actions[i][1], rounding_digits)}{suffix})")
                elif actions[i][0] == 1:
                    print(f"{drive_base_name}.straight({actions[i][1]}{suffix})")
                elif actions[i][0] == 2:
                    print(f"{drive_base_name}.curve({actions[i][1]}, {actions[i][2]}{suffix})")
            break

        elif Button.LEFT in buttons:
            mode = "curve"
            hub.display.char("C")

        elif Button.RIGHT in buttons:
            mode = "straight"
            hub.display.char("S")

run_task(track_movement(drive, hub, "drive"))
