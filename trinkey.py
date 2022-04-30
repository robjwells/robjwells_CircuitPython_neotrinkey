from time import sleep
from neopixel import NeoPixel
from touchio import TouchIn


class PixelProxy:
    def __init__(self, pixels, *indices):
        self._pixels = pixels
        assert len(indices) > 0, "PixelProxy must proxy some pixels!"
        self._indices = indices

    def fill(self, colour):
        for idx in self._indices:
            self._pixels[idx] = colour

    def set(self, colour):
        return self.fill(colour)

    def clear(self):
        self.fill(0)

    def flash(self, colour, times=5, duration=0.1):
        for _ in range(times):
            self.fill(colour)
            sleep(duration)
            self.clear()
            sleep(0.1)


class NeoTrinkeyPixels:
    n_pixels = 4

    # Appease Pylance
    top: PixelProxy
    bottom: PixelProxy

    def __init__(self, board, brightness=0.1) -> None:
        self._pixels = NeoPixel(board.NEOPIXEL, n=self.n_pixels, brightness=brightness)
        self.left = PixelProxy(self._pixels, 0, 1)
        self.outer = PixelProxy(self._pixels, 1, 2)
        self.right = PixelProxy(self._pixels, 2, 3)
        self.inner = PixelProxy(self._pixels, 0, 3)
        self._individual = [
            PixelProxy(self._pixels, n)
            for n in range(self.n_pixels)
        ]

    def save(self):
        self._saved_colours = list(self._pixels)  # type: ignore

    def restore(self):
        for idx, colours in enumerate(self._saved_colours):
            self._pixels[idx] = colours

    def fill(self, colour):
        self._pixels.fill(colour)

    def clear(self):
        self.fill(0)

    def flash(self, colour, times=5, duration=0.1):
        self.save()
        for _ in range(times):
            self.fill(colour)
            sleep(duration)
            self.clear()
            sleep(0.1)
        self.restore()

    def __getitem__(self, index):
        return self._pixels[index]

    def __setitem__(self, index, value):
        self._pixels[index] = value

    def __iter__(self):
        yield from self._individual

    def __reversed__(self):
        yield from reversed(self._individual)

    def set_top_and_bottom(self, *, top, bottom):
        self.top = top
        self.bottom = bottom


class NeoTrinkeyPads:
    def __init__(self, board) -> None:
        self.left = TouchIn(board.TOUCH2)
        self.right = TouchIn(board.TOUCH1)

    def get_press(self, delay=0.25):
        if self.either_pressed:
            sleep(delay)
            if self.both_pressed:
                return "BOTH"
            elif self.top_pressed:
                return "TOP"
            elif self.bottom_pressed:
                return "BOTTOM"
        return None

    @property
    def left_pressed(self):
        return self.left.value

    @property
    def right_pressed(self):
        return self.right.value

    @property
    def either_pressed(self):
        return self.left.value or self.right.value

    @property
    def both_pressed(self):
        return self.left_pressed and self.right_pressed

    def set_top_and_bottom(self, *, top, bottom):
        self.top = top
        self.bottom = bottom

    @property
    def top_pressed(self):
        return self.top.value

    @property
    def bottom_pressed(self):
        return self.bottom.value


class NeoTrinkey:
    def __init__(self, board, brightness=0.1):
        self.pixels = NeoTrinkeyPixels(board, brightness)
        self.pads = NeoTrinkeyPads(board)
        self._set_top_and_bottom()

    def _set_top_and_bottom(self):
        self.pixels.outer.fill(0xFFFFFF)
        while True:
            if self.pads.left_pressed:
                left_top = True
                break
            elif self.pads.right_pressed:
                left_top = False
                break

        if left_top:
            self.pads.set_top_and_bottom(top=self.pads.left, bottom=self.pads.right)
            self.pixels.set_top_and_bottom(top=self.pixels.left, bottom=self.pixels.right)
        else:
            self.pads.set_top_and_bottom(top=self.pads.right, bottom=self.pads.left)
            self.pixels.set_top_and_bottom(top=self.pixels.right, bottom=self.pixels.left)

        self.pixels.clear()
        self.pixels.top.flash(0x004000)
        self.pixels.bottom.flash(0x000040)
