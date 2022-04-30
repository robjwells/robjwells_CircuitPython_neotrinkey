# SPDX-FileCopyrightText: Copyright (c) 2022 Rob Wells
#
# SPDX-License-Identifier: MIT
from typing import Any, Iterator

from neopixel import NeoPixel
from touchio import TouchIn

class PixelProxy:
    """Group an arbitrary set of neopixels to be treated as one."""

    def __init__(self, pixels: NeoPixel, *indices: int) -> None:
        """Set up the proxy for the given indices into the neopixel strip.

        :param pixels: The NeoPixel object for the entire strip.
        :type pixels: NeoPixel
        :param indices: The indices of the relevant pixels on the strip.
        :type indices: int, >= 0 and < `len(pixels)`
        """
    def fill(self, colour: int) -> None:
        """Fill the neopixel(s) with the given colour.

        :param colour: The colour to set the neopixel(s).
        :type colour: int representing a six-hex-digit RGB colour
            (ie `0x000000` to `0xFFFFFF`).
        """
    def set(self, colour: int) -> None:
        """Fill the neopixel(s) with the given colour, alias to `fill`."""
    def clear(self) -> None:
        """Turn off the neopixel(s)."""
    def flash(self, colour: int, times: int, duration: float) -> None:
        """Flash the neopixel(s) with a given colour and duration several times.

        :param colour: The colour to set the neopixel(s).
        :type colour: int representing a six-hex-digit RGB colour
            (ie `0x000000` to `0xFFFFFF`).
        :param times: The number of times to turn on the neopixel(s).
        :type times: int, > 0
        :param duration: The duration in seconds to light the neopixel(s) each flash.
        :type duration: float, fractional seconds.
        """

class NeoTrinkeyPixels:
    """Convenience wrapper around the neopixel buffer."""

    n_pixels: int = 4

    left: PixelProxy
    """A group of pixels 0 and 1, on the left of the board with the pads at the top."""
    outer: PixelProxy
    """A group of pixels 1 and 2, furthest away from the USB port."""
    right: PixelProxy
    """A group of pixels 2 and 3, on the right of the board with the pads at the top."""
    inner: PixelProxy
    """A group of pixels 0 and 3, closest to the USB port."""

    top: PixelProxy
    """A group of two pixels, either `left` or `right` depending on user input during init.

    The purpose of top is to allow consistent input and output relative
    to the user when the NeoTrinkey is plugged in to, eg, the side of a
    laptop.
    """
    bottom: PixelProxy
    """A group of two pixels, either `left` or `right` depending on user input during init.

    The purpose of bottom is to allow consistent input and output
    relative to the user when the NeoTrinkey is plugged in to, eg,
    the side of a laptop.
    """

    def __init__(self, board: Any, brightness: float = ...) -> None:
        """Set up the four neopixels on the board.

        :param board: the CircuitPython `board` module allowing pin access.
        :type board: module
        :param brightness: The brightness setting for the neopixels.
        :type brightness: float, > 0 and <= 1.
        """
    def set_top_and_bottom(self, *, top: PixelProxy, bottom: PixelProxy) -> None:
        """Set which neopixels are at the top and bottom."""
    def fill(self, colour: int) -> None:
        """Fill the neopixel(s) with the given colour.

        :param colour: The colour to set the neopixel(s).
        :type colour: int representing a six-hex-digit RGB colour
            (ie `0x000000` to `0xFFFFFF`).
        """
    def clear(self) -> None:
        """Turn of all the neopixels."""
    def flash(self, colour: int, times: int = ..., duration: float = ...) -> None:
        """Flash all four neopixels with a given colour and duration several times.

        :param colour: The colour to set the neopixel(s).
        :type colour: int representing a six-hex-digit RGB colour
            (ie `0x000000` to `0xFFFFFF`).
        :param times: The number of times to turn on the neopixel(s).
        :type times: int, > 0
        :param duration: The duration in seconds to light the neopixel(s) each flash.
        :type duration: float, fractional seconds.
        """
    def save(self) -> None:
        """Store the current state of the neopixels."""
    def restore(self) -> None:
        """Restore the state of the neopixels."""
    def __getitem__(self, index: int) -> tuple[int, int, int]:
        """Get the colour of the neopixel at the given index."""
    def __setitem__(self, index: int, value: int) -> None:
        """Set the colour of the neopixel at the given index."""
    def __iter__(self) -> Iterator[PixelProxy]:
        """Iterate over proxies for all of the neopixels."""
    def __reversed__(self) -> Iterator[PixelProxy]:
        """Iterate over proxies for all of the neopixels in reverse order."""

# Emulate an enum for the pad press types.
class PadPress:
    """Empty object to represent a particular kind of pad pres."""

class Press:
    """Wrapper around PadPress objects acting as a pseudo-enum."""

    TOP: PadPress
    """The top pad relative to the user when the device is inserted horizontally."""
    BOTTOM: PadPress
    """The bottom pad relative to the user when the device is inserted horizontally."""
    BOTH: PadPress
    """Both touch pads."""

class NeoTrinkeyPads:
    """Convenience wrapper around the two touch input pads."""

    left: TouchIn
    """The left-hand pad when the device is oriented with the pads at the top."""
    right: TouchIn
    """The right-hand pad when the device is oriented with the pads at the top."""

    top: TouchIn
    """The top pad relative to the user when the device is inserted horizontally."""
    bottom: TouchIn
    """The bottom pad relative to the user when the device is inserted horizontally."""

    def __init__(self, board: Any) -> None:
        """Set up the touch pads.

        :param board: The `board` CircuitPython module, allowing pin access.
        :type board: module
        """
    def get_press(self, delay: float = ...) -> PadPress | None:
        """Return the current press state as as pseudo-enum.

        :param delay: A short delay to make it easier to press both pads at once.
        :type delay: float, fractional seconds
        :return: An object representing which pad was pressed (or both),
            which must be matched against the class variables of `Press`,
            or `None` if neither of the pads were pressed.
        :rtype: A PadPress object, effectively just `object()`, or None.
        """
    def set_top_and_bottom(self, *, top: TouchIn, bottom: TouchIn) -> None:
        """Set which pad is at the top and which is at the bottom."""
    # Properties
    left_pressed: bool
    right_pressed: bool
    either_pressed: bool
    both_pressed: bool
    top_pressed: bool
    bottom_pressed: bool

class NeoTrinkey:
    """Convenience wrapper around the NeoTrinkey's touch pads and neopixels."""

    pixels: NeoTrinkeyPixels
    pads: NeoTrinkeyPads

    def __init__(self, board: Any, brightness: float = ...) -> None:
        """Set up the board with a given brightness and set the top & bottom pads and pixels.

        :param board: The `board` CircuitPython module, allowing pin access.
        :type board: module
        :param brightness: The brightness to set the neopixels.
        :type brightness: float, > 0 and <= 1.
        """
    def _set_top_and_bottom(self) -> None:
        """Set which side of the board is at the top, giving top/bottom pads and pixels.

        This is called as part of the class initialisation but could be called again
        if you have some use for changing the orientation of the board.
        """
