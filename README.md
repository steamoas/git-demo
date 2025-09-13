# pybricks-program-switcher

A template library to easily switch between different functions using the hub's arrow keys.

# usage
## getting started
1: clone the repo and open the folder in your IDE of choice

2: update robot.py with all the motors/sensors and drive base relevant to your robot

3: in other programs, import every robot function (hub, drive_base, left_motor, etc.) from robot.py rather than defining it

## using the switcher
```
# import all devices that you need
from robot import hub, drive_base, left_motor, right_motor
```
Use the robot functions you imported to build your program (see example_programs.py for examples)

Once you have made your programs, add them to the switcher in main.py. You can also optioanlly add a function that will be called at the start of each run:

```
from program_switcher import ProgramSwitcher
from robot import hub, drive_base
from example_programs import drive_forever, turn_left, turn_right

def run_start_function():
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=600, turn_rate=250)

switcher = ProgramSwitcher(hub)

switcher.add_run_start_function(run_start_function)
switcher.add_program(drive_forever)
switcher.add_program(turn_left)
switcher.add_program(turn_right)
```

Run the switcher

```
switcher.run()
```
