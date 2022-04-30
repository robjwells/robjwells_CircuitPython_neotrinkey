from time import sleep
import board
from supervisor import runtime
from rainbowio import colorwheel

from trinkey import NeoTrinkey
from colours import *


def start_up(trinkey):
    for p in trinkey.pixels:
        p.fill(0x100000)
        sleep(0.25)
    for p in reversed(trinkey.pixels):
        p.clear()
        sleep(0.25)


trinkey = NeoTrinkey(board)
start_up(trinkey)
all_on = False

trinkey.pixels.fill(0xFF0000)

while True:
    if runtime.serial_bytes_available:
        command = input()
        ps, cs = command.split(";")
        pixels_to_set = [int(x) for x in ps.split(",")]
        colour = int(cs, 16)
        for p in pixels_to_set:
            trinkey.pixels[p] = colour

    pressed = trinkey.pads.get_press()
    if pressed == "TOP":
        trinkey.pixels.flash(green)
    elif pressed == "BOTTOM":
        trinkey.pixels.flash(blue)
    elif pressed == "BOTH":
        trinkey.pixels.flash(0xffffff)
