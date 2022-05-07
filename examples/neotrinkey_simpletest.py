# SPDX-FileCopyrightText: Copyright (c) 2022 Rob Wells
#
# SPDX-License-Identifier: MIT
import gc

import board

from robjwells_neotrinkey import NeoTrinkey, StatusMonitor

BLUE = 0x00_00_FF
GREEN = 0x00_FF_00


def flash_blue(trinkey: NeoTrinkey, update=None, pad=None):
    trinkey.pixels.flash(BLUE)


def flash_green(trinkey: NeoTrinkey, update=None, pad=None):
    trinkey.pixels.flash(GREEN)


trinkey = NeoTrinkey(board)
monitor = StatusMonitor(trinkey, serial_handler=flash_blue, touch_handler=flash_green)

gc.collect()
print("Free: {:,}kB\tUsed: {:,}kB".format(gc.mem_free(), gc.mem_alloc()))
# Just over 10kB of memory free.

monitor.run()
