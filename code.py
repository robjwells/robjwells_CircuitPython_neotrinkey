from time import sleep
import board
from supervisor import runtime
from neopixel import NeoPixel
from rainbowio import colorwheel
from micropython import const  # type: ignore
from touchio import TouchIn

N_NEOPIXELS = const(4)
pixels = NeoPixel(board.NEOPIXEL, N_NEOPIXELS, brightness=0.1)

LEFT_TOUCH = TouchIn(board.TOUCH2)
LEFT_SIDE = (0, 1)
RIGHT_TOUCH = TouchIn(board.TOUCH1)
RIGHT_SIDE = (2, 3)

INNER_SIDE = (0, 3)
OUTER_SIDE = (1, 2)

def fill(side, colour):
    for i in side:
        pixels[i] = colour

fill(OUTER_SIDE, 0x0000FF)
while True:
    if LEFT_TOUCH.value:
        TOP_TOUCH = LEFT_TOUCH
        TOP_SIDE = LEFT_SIDE
        BOTTOM_TOUCH = RIGHT_TOUCH
        BOTTOM_SIDE = RIGHT_SIDE
        break
    elif RIGHT_TOUCH.value:
        TOP_TOUCH = RIGHT_TOUCH
        TOP_SIDE = RIGHT_SIDE
        BOTTOM_TOUCH = LEFT_TOUCH
        BOTTOM_SIDE = LEFT_SIDE
        break
pixels.fill(0)

while True:
    if TOP_TOUCH.value and BOTTOM_TOUCH.value:
        pixels.fill(0)
    if runtime.serial_bytes_available:
        command = input()
        ps, cs = command.split(";")
        pixels_to_set = [int(x) for x in ps.split(",")]
        colour = int(cs, 16)
        for p in pixels_to_set:
            pixels[p] = colour
