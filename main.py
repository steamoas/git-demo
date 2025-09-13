from program_switcher import ProgramSwitcher
from robot import hub, drive_base
from example_programs import drive_forever, turn_left, turn_right

#example_program, adapt to fit your use case

def run_start_function():
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=600, turn_rate=250)

switcher = ProgramSwitcher(hub)

switcher.add_run_start_function(run_start_function)
switcher.add_program(drive_forever)
switcher.add_program(turn_left)
switcher.add_program(turn_right)

switcher.run()
