..
    # SPDX-FileCopyrightText: Copyright (c) 2022 Rob Wells
    #
    # SPDX-License-Identifier: MIT

Introduction
============

.. image:: https://readthedocs.org/projects/robjwells-circuitpython-neotrinkey/badge/?version=latest
    :target: https://circuitpython-neotrinkey.readthedocs.io/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/robjwells/robjwells_CircuitPython_neotrinkey/workflows/Build%20CI/badge.svg
    :target: https://github.com/robjwells/robjwells_CircuitPython_neotrinkey/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

This library wraps the Adafruit `Neo Trinkey`_ (or NeoPixel Trinkey),
providing helpers for using the NeoPixels and touch pads. It also
includes a class to make using the Neo Trinkey as a status monitor for a
host computer very easy, through the use of callback functions for touch
and serial inputs.

.. _Neo Trinkey: https://www.adafruit.com/product/4870

Dependencies
=============

This library only depends on `CircuitPython`_.
The build for the Neo Trinkey includes all needed dependencies.

.. _CircuitPython: https://circuitpython.org/board/neopixel_trinkey_m0/

Usage Example
=============

Here’s a bare-bones example that flashes all the LEDs blue when a serial
message is received, and green when either of the touch pads are pressed.

.. literalinclude:: ../examples/neotrinkey_simpletest.py

Documentation
=============

API documentation for this library can be found on `Read the Docs
<https://robjwells-circuitpython-neotrinkey.readthedocs.io/>`_.

Contributing
============

Contributions are welcome! Please open an issue or submit a pull request.
