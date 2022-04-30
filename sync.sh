# SPDX-FileCopyrightText: Copyright (c) 2022 Rob Wells
#
# SPDX-License-Identifier: MIT
fd . -e py -e mpy -e json \
    --exec-batch rsync --archive --relative --verbose "{}" /Volumes/CIRCUITPY/
