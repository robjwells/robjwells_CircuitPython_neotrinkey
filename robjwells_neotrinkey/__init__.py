# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Rob Wells
#
# SPDX-License-Identifier: MIT
"""
`robjwells_neotrinkey`
================================================================================

Convenience wrappers for the Neopixel Trinkey.


* Author(s): Rob Wells

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/robjwells/robjwells_CircuitPython_neotrinkey.git"

from ._neotrinkey import NeoTrinkey, PadPress, Press
from .status import (
    StatusMonitor,
    SectionUpdate,
)

__all__ = [
    "NeoTrinkey",
    "PadPress",
    "Press",
    "StatusMonitor",
    "SectionUpdate",
]
