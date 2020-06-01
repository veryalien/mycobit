# mycobit

A 4-bit computer system for the microbit.

Mycobit is a microbit implementation of the MyCo (My little Computer) system, also known in german as TPS (Tastenprogrammierbare Steuerung).

You can create, save and run useful programs directly on the microbit, without needing a computer connected at all.
Once mycobit has been installed on the microbit you can program using only the three buttons A, B and reset!

For a complete guide to MyCo/TPS you can have a look at the german site: http://www.elektronik-labor.de/Lernpakete/TPS/TPS0.html

At that site you'll see that TPS has a long history, going back over a number of years.

I bought this [Microcontroller Pack](https://www.conrad.com/p/conrad-components-10104-profi-mikrocontroller-course-material-14-years-and-over-192286 "Conrad TPS Pack") from Conrad and I was hooked.

I apolgise profusely for the state of the 'denglisch' on the Conrad page, it might be actually be 'double Dutch', but never mind!

I live in Germany (over 20 years), so it's not that much of a problem for me to understand the original documentation.

For a lot of useful information in english I suggest that you download this pdf: http://www.elektronik-labor.de/Literatur/MyCo2014.pdf

Please note that the instruction table is very strangely formatted and doesn't contain all of the proper instruction descriptions.

That is a free excerpt from a complete instruction manual which you can still purchase from amazon.

Mycobit is fully backwards-compatible with the MyCo/TPS systems. There are a few enhancements to support the larger microbit display and available memory. The input and output pins have been assigned according to the microbit edge connector analogue and digital pins.

# Limitations

The '4 bit' implementation was strictly observed, the microbit display is not used with the built-in display features to scroll messages and show images. Only the top-right hand 4 x 4 pixels are used as a display, but it is still very useful. Light-sensing, via the display leds, is also not available.

No SPI or I2C devices are supported. The SPI pins have been used as GPIO pins. I2C will probably not be supported.

Unfortunately micropython on the microbit's nrf51822 doesn't leave much memory free and it was a struggle to get the final mycobit.py to be loaded successfully without any memory errors. The source has virtually no comments and lots of pretty whitespace and variable names have been manually omitted, minifying the source didn't make any difference any more.
There are a couple of enhanced shift and rotate instructions commented out in the code as they simply make the python too large or complex for it to be successfully compiled to byte-code when loaded.

I've also made an (unpublished) implementation for the banana pi bpi:bit, called mycobpibit, which includes these new instructions. The bpi:bit uses an esp32 and there is simply more free runtime memory available for micropython.

# Getting Started

A quick start-up guide to getting mycobit running on your microbit.

# Installation

The initial version of mycobit is written in micropython, not makecode.
So you'll need an editor for vanilla microbit micropython.

I recommend using the python mu editor as it will handle installing micropython automatically.

Load up the mycobit.py file in mu and download it to your microbit.

Reset your microbit, and let's get started with mycobit programming!

# First steps in the editor
There's nothing on the display, is it dead?
No, it's not dead, it's just doing nothing. We need to add a mycobit program.

Keep button B held down and press and release the reset button.
When the microbit restarts four of the top leds will light up. We're in the mycobit editor!
Release button B and the leds will turn off.

The highlighted leds are the editor 'cursor'. Showing you which nibble is to be edited.

Press and release button A and nothing happens!? Actually zero was put in the frst nibble.

Press and release button A again and one led  will be displayed in the top right-hand corner of the display. Now the value 1 is in the first nibble.
Hold button A down and it will cycle through all 16 values. Wow, action!

Pressing button B will move to the next nibble, it will be highlighted with the cursor.
Hold down button B and it will move through the mycobit memory.
Note: You cannot move backwards in memory, we've only got buttons A, B and reset!

As the cursor moves through the memory you'll see some leds light up on the left and bottom of the display. These indicate the byte address in mycobit memory.
The left column indicates the byte we are editing. The display shows two bytes, split into four nibbles. So two of the nibbles have the same byte address.
The bottom row indicates which page we are editing. mycobit memory is split into 16 bytes in 16 pages. Address space of 256 bytes, wow!

The left column will count from 0 to 15 (top to bottom), depending on the byte being edited.
The bottom row will count from 0 to 15 (right to left - to match the nibble values), depending on the page.
You'll get used to it!

# First Program Tutorial

Reset the microbit with button B held down to get back into the editor at byte 0.

Instructions go in the first nibble of each byte.

Press button A twice so the value 1 is shown on the top row of leds: ``. . . . O``
The first press puts zero in the nibble, which you obviously can't see.
The instruction 1 shows a value on the display at runtime.

Press button B (don't hold) to highlight the second nibble.

Data values go in the second nibble of each byte.
For instruction 1, the data will be the value displayed.

Press button A until the value 10 (0x0A) is displayed: ``. O . O .``
That will be 11 individual presses - including zero at the start.
 
The second instruction will be a relative jump to itself to 'stop' the program.

Press button B to highlight the third row of leds, the top left led lights up, we are editing byte 1.

Press button A until the value 3 is displayed: ``. . . O O``

Press button B to highlight the fourth row of leds.

Press button A once, not really needed when the memory is empty, but this puts zero into the nibble.

Now your complete microbit display should look like this (including the memory counters):

``o . . . O`` <br/>
``. O . O .`` <br/>
``. . . O O`` <br/>
``. . . . .`` <br/>
``. . . . .`` <br/>

Note that the memory counters are shown dimmer than the contents of memory.

The overall editor display looks like this:

``b . . . .`` <br/>
``y . . . .`` <br/>
``t . . . .`` <br/>
``e . . . .`` <br/>
``. e g a p`` <br/>

'egap' is page backwards as we count the bytes from right to left to match the way nibble values are displayed!


# Saving and running that first program

We've got a program in the editor, but now we need to run it.
First, you need to save that program to the microbit flash.
Hold down button B. The editor will start scrolling through memory. This is ok, we are only viewing not editing.
While holding down button B, hold down button A until the display clears.
The program has now been saved in the microbit.
Release both buttons.

If everything worked correctly you'll see the value 10 (0x0A) displayed on the lop row of leds: ``. O . O .``

Wow, amazing, it worked!

# Running a stored program

To run a stored program, just turn on the microbit and the program will run, that's it!

If you click the reset button on the back of microbit without any buttons pressed, the saved program will also run.

# Editing a saved program

To edit a saved program, just reset the microbit with button B held down. Release the button when you see the display.
You're now in the editor which shows your stored program.

Enjoy!

# Example Program - binary counter

Here's a very simple little example program just to give you a taste of programming mycobit with a bit more action.
It will show a little binary counter on the top row of the display.

Enter the following sequence of binary nibble values in the editor:

5 - move the contents of register A to ... <br/>
4 - the display

7 - A = ... <br/>
1 - A + 1

2 - wait ... <br/>
8 - 500 ms

3 - relative jump backwards ... <br/>
3 - 3 bytes (jump to the first instruction '54')

Save the program and watch the binary numbers cycle around from 0 to 15, forever!

You can edit the program and change the wait time between counts from 0 = 1 ms to 15 = 60s.


# What do all those mycobit instructions do?

Good question, more info coming soon!

See mycobit_info.pdf for the complete, but mostly unexplained, instruction set.

# 'Default' MyCo/TPS programs

Note: To make full use of the demo programs you will need some kind of breakout board (bob) for your bit, so you can access all of the pins on the edge connector. Without any breakout board you'll just see some blinking leds as that is the default MyCo/TPS demo without any input pins set to the correct state.

The original MyCo/TPS system came with a set of built-in demo programs and subroutines.
You can find exactly the same mycobit programs here in the file called 'default'.

MyCo/TPS has a nifty way to get back to a known state by re-loading the original demo programs from a hidden part of memory.
This behaviour is also implemented in mycobit, but you need to copy the 'default' file to the microbit.
The easiest way is to get the 'default' file from this repository and copy it to your mu-code directory.

Use the mu files tab to show the files on your microbit. On the left you'll see the list of files on your microbit, most probably just main.py (mycobit.py is renamed after it's copied) and any programs you've saved in the file 'mycobit'.
 Programs are saved and loaded to and from the microbit micropython file system using a file called 'mycobit'.

On the right side, mu will show the list of files on your computer, if you've copied 'default' to your mu-code directory it will appear here.

Drag the 'default' file onto the microbit file list. It will be copied over to the microbit. You only have to do this once, or after you've been using your microbit for other things and the micropython file system got re-flashed.

Now you can use the editor to load the default mycobit programs whenever you want, this will however completely overwrite any stored programs in the file 'mycobit'.

Reloading the default programs is as simple as going into the editor and setting the first four nibbles of memory to 15 (0x0F). Go into the mycobit editor and set everything to 1 bits, it will end up looking like this:

``o O O O O`` <br/>
``. O O O O`` <br/>
``. O O O O`` <br/>
``. O O O O`` <br/>
``. . . . .`` <br/>

Now press and hold button B, while holding press button A. This will save 0xFF 0xFF as a program, but when this is reloaded mycobit will see it as a magic reset number. 0xFF 0xFF can never occur as the first two bytes in a real mycobit program.

mycobit will now load the default programs from the file 'default' into the 'mycobit' file. You've lost your program, but now you've got the demo programs loaded - more details on using the demos coming soon!

If you see the top row left and right pixels blinking then it's working! Without any breakout board, it won't help much to begin with.

If you go into the editor (reset with button B pressed) you'll now see the first four nibbles of the demo program instead of 0xF 0xF 0xF 0xF.

``. . O O .`` <br/>
``. . O . .`` <br/>
``. . O . O`` <br/>
``. . . . O`` <br/>

6 - A= ... <br/>
4 - Din - read the digital input pins (to select the relevant demo)

5 - move the contents of register A to ... <br/>
1 - register B

You can now continue using mycobit as before, you can browse through the demo programs and try to work out what they do. Read the MyCo documents which explains them in detail. Otherwise you can just go into the editor and overwrite the demo program code with your own.

If you ever need to get back to a known state just follow these instructions again and the default programs will be re-loaded.


# Can mycobit use the edge connector pins on the microbit?

It can and it does, both analogue and digital inputs and outputs are supported. 

