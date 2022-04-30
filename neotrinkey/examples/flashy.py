from time import sleep
import board

from neotrinkey import NeoTrinkey, PadPress, Press, SectionUpdate, StatusMonitor
import colours


def fill_and_drain(
    trinkey: NeoTrinkey, colour: int = colours.low_red, delay: float = 0.25
) -> None:
    for p in trinkey.pixels:
        p.set(colour)
        sleep(delay)
    for p in reversed(trinkey.pixels):
        p.clear()
        sleep(delay)


def chase(
    trinkey: NeoTrinkey, colour: int = colours.low_red, delay: float = 0.25
) -> None:
    for active in trinkey.pixels:
        trinkey.pixels.clear()
        active.set(colour)
        sleep(delay)


trinkey = NeoTrinkey(board)
fill_and_drain(trinkey)

trinkey.pixels.top.fill(colours.low_blue)
trinkey.pixels.bottom.fill(colours.low_green)


def serial(trinkey: NeoTrinkey, update: list[SectionUpdate]) -> None:
    cs = [colours.pink, colours.yellow, colours.teal, colours.purple]
    for c in cs[: len(update)]:
        trinkey.pixels.flash(c)


def touch(trinkey: NeoTrinkey, pad: PadPress) -> None:
    if pad is Press.BOTTOM:
        trinkey.pixels.flash(colours.green)
    elif pad is Press.TOP:
        trinkey.pixels.flash(colours.blue)
    elif pad is Press.BOTH:
        trinkey.pixels.flash(colours.white)


monitor = StatusMonitor(trinkey, serial, touch)
monitor.run()
