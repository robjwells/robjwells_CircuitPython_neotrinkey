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
    def __init__(self, neotrinkey, serial_handler, touch_handler):
        self.trinkey = neotrinkey
        self.serial = serial_handler
        self.touch = touch_handler

    def run(self):
        while True:
            press = self.trinkey.pads.get_press()
            if press is not None:
                print("Pressed: %s" % press)
                self.touch(trinkey=self.trinkey, pad=press)
            serial_update = read_serial_update()
            if serial_update:
                print("Serial: %s" % serial_update)
                self.serial(trinkey=self.trinkey, update=serial_update)
