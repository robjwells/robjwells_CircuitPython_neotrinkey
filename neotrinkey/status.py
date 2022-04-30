from collections import namedtuple
from supervisor import runtime

SectionUpdate = namedtuple("SectionUpdate", ("name", "value"))


def process_command_line(line):
    parts = [section.split("=") for section in line.split(";")]
    return [SectionUpdate(section_name, float(value)) for section_name, value in parts]


def read_serial_update():
    if not runtime.serial_bytes_available:
        return []
    return process_command_line(input())


class StatusMonitor:
    def __init__(self, neotrinkey, serial_handler=None, touch_handler=None):
        self.trinkey = neotrinkey
        self.serial = serial_handler
        self.touch = touch_handler

    def run(self):
        while True:
            if self.touch is not None:
                press = self.trinkey.pads.get_press()
                if press is not None:
                    self.touch(trinkey=self.trinkey, pad=press)
            if self.serial is not None:
                serial_update = read_serial_update()
                if serial_update:
                    self.serial(trinkey=self.trinkey, update=serial_update)
