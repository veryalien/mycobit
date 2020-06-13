# myconanobit

This version of mycobit is for the Kittenbot nanobit, a micro:bit in an Arduino nano compatible pin package.

This is currently just a proof of concept version as there are a few show-stoppers, but it's possible to use with huge workarounds...

#### No Display

There is no built-in LED matrix on the nanobit. However, all the row and column pins are accessible, so you could build one yourself.
The only issue there is that the micro:bit has a 5x5 LED matrix display but it's actually accessed as a 3x9 matrix with 2 LEDs missing on one row!
There is at least one breakout board for the nanobit that adds a LED matrix, but this only seems to be available in Thailand.
I'm in the process of laying out a breadboard version of an add-on LED matrix, I'll report back when it's all working.

#### No (visible) built-in editor

As there is no LED matrix you cannot edit any programs, you cannot see what you are editing!
You cannot even easily try to load the 'default' programs because you will not be able to see if you have correctly entered F F F F to reset to default.
But there is a relatively simple solution, use the Dout pins as a 4-bit display. This is exactly what the original TPS did!
The current version does not have the editor and default output modified to work with the Dout port, changes are in progress.

#### Tiny buttons A and B

The nanobit does have two built-in buttons, which are exactly the same as buttons A and B on the micro:bit. Trouble is, they are very tiny buttons right next to each other mounted in the middle of the board, not easily accessible. Luckily there are some pads available to add some external buttons which will make them much easier to use. This requires soldering and I will need to try it myself first.

#### hexedit to the rescue

So without a nice display and easy-to-use buttons, how can you use myconanobit with your own edited programs? 
There is a tiny linux hexadecimal file editor that I use to modify the 'default' and 'mycobit' program files directly. You can load up a 'mycobit' file and edit each nibble, quickly and easily, rather than using any buttons on the nanobit. Transfer the current 'mycobit' from the nanobit to your computer using mu or mpfs, edit the 'mycobit' in hexedit, save and then transfer the file back to the nanobit using mu or mpfs.
It's not very pretty, but it works!

#### Lack of memory space

For some strange reason I could not get the mycobit program to fit in the memory of the nanobit. This is a bit strange as it's exactly the same processor as the micro:bit. I think it might be due to different (older) firmware which leaves slightly less memory available for micropython.

What I've done in this version is to reduce the memory space to 8 Pages, which is exactly the same as the original TPS board (128 bytes). You can run all of the TPS programs, but some fancy mycobit features will not work, like accessing characters in the extended memory space.

In fact this version will be very easy to crash as there are currently no stringent memory bounds checks, so if you try to address any memory in Pages 8 - 15, it will crash with a nasty micropython out of bounds error or something similar. This should be extremely easy to fix, as long as the python code doesn't get too large to be successfully loaded and compiled at boot.

#### Proof of concept up and running

The myconanobit program runs successfully on the nanobit using micro:bit micropython. The 'default' and 'mycobit' files in the myconanobit folder are specifically for use with myconanobit and the 'default' program output has been changed to use the Dout pins 1, 2, 8 and 12. The editor part of the program still needs to be modified as do the commands to display immediate values and so on. Work in progress.

