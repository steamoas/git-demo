from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import multitask, wait, run_task

class ProgramSwitcher:
    def __init__(self, hub):
        self.hub = hub
        self.program_list = []
        self.setup_function = None

    def add_run_start_function(self, function):
        self.setup_function = function

    def add_program(self, program):
        self.program_list.append(program)


    def run(self, wait_time_ms : int = 150, start_button:Button = Button.CENTER):

        current_run = 0
        while True:
            buttons = self.hub.buttons.pressed()

            if Button.LEFT in buttons:
                if current_run == 0:
                    current_run = len(self.program_list) - 1
                else:
                    current_run -= 1

            if Button.RIGHT in buttons:
                if current_run == len(self.program_list) - 1:
                    current_run = 0
                else:
                    current_run += 1

            self.hub.display.number(current_run)

            if start_button in buttons:
                if self.setup_function:
                    self.setup_function()

                run_task(self.program_list[current_run]())

            else:
                wait(wait_time_ms)
