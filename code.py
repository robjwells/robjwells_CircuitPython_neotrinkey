from time import sleep
import board

from neotrinkey import NeoTrinkey, PadPress, Press
from colours import *

from neotrinkey_status import SectionUpdate, read_serial_update, StatusMonitor


def fill_and_drain(
    trinkey: NeoTrinkey, colour: int = low_red, delay: float = 0.25
) -> None:
    for p in trinkey.pixels:
        p.set(colour)
        sleep(delay)
    for p in reversed(trinkey.pixels):
        p.clear()
        sleep(delay)


def chase(trinkey: NeoTrinkey, colour: int = low_red, delay: float = 0.25) -> None:
    for active in trinkey.pixels:
        trinkey.pixels.clear()
        active.set(colour)
        sleep(delay)


trinkey = NeoTrinkey(board)
fill_and_drain(trinkey)

trinkey.pixels.top.fill(low_blue)
trinkey.pixels.bottom.fill(low_green)


def serial(trinkey: NeoTrinkey, update: list[SectionUpdate]) -> None:
    colours = [pink, yellow, teal, purple]
    for colour in colours[: len(update)]:
        trinkey.pixels.flash(colour)


def touch(trinkey: NeoTrinkey, pad: PadPress) -> None:
    if pad is Press.BOTTOM:
        trinkey.pixels.flash(green)
    elif pad is Press.TOP:
        trinkey.pixels.flash(blue)
    elif pad is Press.BOTH:
        trinkey.pixels.flash(white)


monitor = StatusMonitor(trinkey, serial, touch)
monitor.run()
