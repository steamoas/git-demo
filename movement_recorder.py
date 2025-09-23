from pybricks.hubs import PrimeHub
from robot import drive_base
from robot import hub
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait, run_task

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
    print("To begin tracking, press your hub's center button.")
    print("When you want to finish tracking, press the button again. Your movements will be recorded to the console.")
    print("To generate python instructions for your tracked movements, press the bluetooth button.")
    print("To exit, press the left and right arrow buttons simultaneously")

    actions = []
    actions_count = 0

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

            if abs(end_angle * 10) > abs(end_distance):
                actions.append((0, end_angle))
                print(f"{actions_count}: turn {end_angle} degrees")
            else:
                actions.append((1, end_distance))
                print(f"{actions_count}: drive {end_distance} mm")

            actions_count += 1
            hub.light.on(Color.GREEN)
            wait(250)


        elif Button.BLUETOOTH in buttons:
            print("Generating python code:\n")
            suffix = f", then = {stop_type}" if stop_type != Stop.HOLD else ""
            for i in range(actions_count):
                if actions[i][0] == 0:
                    print(f"{drive_base_name}.turn({round(actions[i][1], rounding_digits)}{suffix})")
                else:
                    print(f"{drive_base_name}.straight({actions[i][1]}{suffix})")
            break
run_task(track_movement(drive_base, hub))
