import gc

import board

from neotrinkey import NeoTrinkey, StatusMonitor


def no_op(*args, **kwargs):
    pass


trinkey = NeoTrinkey(board)

monitor = StatusMonitor(trinkey, no_op, no_op)

gc.collect()
print("Free: {:,}kB\tUsed: {:,}kB".format(gc.mem_free(), gc.mem_alloc()))
# Just over 10kB of memory free.

monitor.run()
