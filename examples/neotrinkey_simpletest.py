import gc

import board

from neotrinkey import NeoTrinkey, StatusMonitor


def flash_blue(trinkey: NeoTrinkey, update=None, pad=None):
    trinkey.pixels.flash(0x0000FF)


def flash_green(trinkey: NeoTrinkey, update=None, pad=None):
    trinkey.pixels.flash(0x00FF00)


trinkey = NeoTrinkey(board)

monitor = StatusMonitor(trinkey, flash_blue, flash_green)

gc.collect()
print("Free: {:,}kB\tUsed: {:,}kB".format(gc.mem_free(), gc.mem_alloc()))
# Just over 10kB of memory free.

monitor.run()
