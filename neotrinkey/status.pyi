from typing import NamedTuple, NoReturn, Protocol
from ._neotrinkey import NeoTrinkey, PadPress

class SectionUpdate(NamedTuple):
    name: str
    value: float

class SerialCallback(Protocol):
    def __call__(self, trinkey: NeoTrinkey, update: list[SectionUpdate]) -> None: ...

class TouchCallback(Protocol):
    def __call__(self, trinkey: NeoTrinkey, pad: PadPress) -> None: ...

def process_command_line(line: str) -> list[SectionUpdate]: ...
def read_serial_update() -> list[SectionUpdate]: ...

class StatusMonitor:
    trinkey: NeoTrinkey
    serial: SerialCallback
    touch: TouchCallback

    def __init__(
        self,
        neotrinkey: NeoTrinkey,
        serial_handler: SerialCallback,
        touch_handler: TouchCallback,
    ) -> None: ...
    def run(self) -> NoReturn: ...
