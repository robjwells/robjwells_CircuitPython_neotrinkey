from typing import NamedTuple, NoReturn, Protocol
from ._neotrinkey import NeoTrinkey, PadPress

class SectionUpdate(NamedTuple):
    """A name-value pair parsed from serial input."""

    name: str
    value: float

class SerialCallback(Protocol):
    def __call__(self, trinkey: NeoTrinkey, *, update: list[SectionUpdate]) -> None:
        """Callback function for serial input.

        :param trinkey: the wrapper around the board's neopixels and pads.
        :type trinkey: NeoTrinkey
        :param update: a list of name, value pair namedtuples extracted from the serial data.
        :type update: list[SectionUpdate]
        """

class TouchCallback(Protocol):
    def __call__(self, trinkey: NeoTrinkey, *, pad: PadPress) -> None:
        """Callback function for touch input.

        :param trinkey: the wrapper around the board's neopixels and pads.
        :type trinkey: NeoTrinkey
        :param pad: object representing the pad (or pads) pressed.
            `pad` should be matched against the class variables of `Press`.
        :type pad: Press
        """

def process_command_line(line: str) -> list[SectionUpdate]:
    """Parse a command line received over serial.

    The command line must be in the format `name_1=float_1;name_2=float_2`,
    with one or more name-value pairs. The values _must_ be numeric as they
    are parsed as `float`s.

    :param line: The input from the serial connection.
    :type line: str
    :return: A list of namedtuples wrapping the name and value pairs.
    :rtype: list[SectionUpdate]
    """

def read_serial_update() -> list[SectionUpdate]:
    """Read and parse data (if any) from the serial connection.

    :return: a list of nametuples wrapping the name and value pairs
        from the serial input. If there were no bytes available on
        the serial connection the list is empty.
    :rtype: list[SectionUpdate]
    """

class StatusMonitor:
    """A monitor that dispatches events to the provided serial and touch callbacks."""

    trinkey: NeoTrinkey
    serial: SerialCallback | None
    touch: TouchCallback | None

    def __init__(
        self,
        neotrinkey: NeoTrinkey,
        serial_handler: SerialCallback | None = None,
        touch_handler: TouchCallback | None = None,
    ) -> None:
        """Set up the monitor with optional serial and touch callbacks.

        If a callback isn't provided for either serial or touch, those events are
        ignored.

        :param trinkey: the convenience wrapper around the board's pixels and pads.
        :type trinkey: NeoTrinkey
        :param serial_handler: a callback function for responding to serial input
        :type serial_handler: a function that takes the NeoTrinkey wrapper and
            a list of parsed name-value pairs from the serial input.
        :param touch_handler: a callback function for responding to touch input
        :type touch_handler: a function that takes the NeoTrinkey wrapper and
            an object representing the kind of touch input, which must be matched
            against the class variables of Press to discriminate between different
            touch inputs.
        """
    def run(self) -> NoReturn:
        """Loop forever, dispatching touch and serial events to callbacks as they occur."""
