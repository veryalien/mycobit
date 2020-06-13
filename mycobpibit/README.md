# mycobpibit

This is the version of mycobit for the banana pi bpi:bit.

There are a few differences to mycobit for the micro:bit as the bpi:bit has a RGB LED 5x5 display. Additional colour commands have been included to allow changing the pixel colours on the display.

You can find the full instruction set and info in the mycobpibit doc folder.

All of the other features of mycobit for the micro:bit will work with mycobpibit, please refer to the main README for more details.

This version will not work on the micro:bit.

mycobpibit is written in micropython, you will need to have micropyhon installed on your bpi:bit to use mycobpibit.

To cut a long story short, if you know what you are doing, the bpi:bit is just an ESP32 board with a set of pre-defined sensors and I/O devices. Use the python esptool program to flash the following micropython firmware on the bpi:bit:

https://github.com/BPI-STEAM/BPI-BIT-MicroPython/releases/download/20190623/firmware-20190623.bin

You can find the original installation instructions here, get ready to use chrome and translate to english:

https://doc.bpi-steam.com/zh_CN/latest/micropython/install&use.html#bpi-bit-micropython

You will need to use a different editor than mu. The bpi:bit will not be recognised correctly. You will need to use something like mpfs to access the micropython file system and transfer the mycobpibit python program to the bpi:bit.
When installing or updating mycobit with a python editor, just remember to always use the mycobpibit.py file, instead of mycobit.py!
Copy the mycobpibit.py file as main.py to the board, it should execute when the bpi:bit is reset.
