from time import sleep
import board

from neotrinkey import NeoTrinkey, PadPress, Press, SectionUpdate, StatusMonitor
import colours


def fill_and_drain(
    trinkey: NeoTrinkey, colour: int = colours.low_red, delay: float = 0.25
) -> None:
    """Set the pixels clockwise from 0 to red, then clear one by one back to 0."""
    for p in trinkey.pixels:
        p.set(colour)
        sleep(delay)
    for p in reversed(trinkey.pixels):
        p.clear()
        sleep(delay)


trinkey = NeoTrinkey(board)
fill_and_drain(trinkey)

trinkey.pixels.top.fill(colours.low_blue)
trinkey.pixels.bottom.fill(colours.low_green)


def serial(trinkey: NeoTrinkey, update: list[SectionUpdate]) -> None:
    """Flash a different colour for each update part received over serial."""
    cs = [colours.pink, colours.yellow, colours.teal, colours.purple]
    for c in cs[: len(update)]:
        trinkey.pixels.flash(c)


def touch(trinkey: NeoTrinkey, pad: PadPress) -> None:
    """Flash a different colour depending on which pad is pressed."""
    if pad is Press.BOTTOM:
        trinkey.pixels.flash(colours.green)
    elif pad is Press.TOP:
        trinkey.pixels.flash(colours.blue)
    elif pad is Press.BOTH:
        trinkey.pixels.flash(colours.white)


monitor = StatusMonitor(trinkey, serial, touch)
monitor.run()
