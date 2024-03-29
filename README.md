# mycobit

A 4-bit computer system for the micro:bit.

Mycobit is a micro:bit implementation of the MyCo (My little Computer) system, also known in german as TPS (Tastenprogrammierbare Steuerung).

You can create, save and run useful programs directly on the micro:bit, without needing a computer connected at all.
Once mycobit has been installed on the micro:bit you can program using only the three buttons A, B and reset!

# Getting Started

A quick start-up guide to getting mycobit running on your micro:bit.

# Easy Installation

Connect your microbit to your computer and you should see a device window called MICROBIT.
 
Download the file mycobit.hex (or mycobitv2.hex if you have a microbit v2) and copy it to your microbit by dragging the file into the MICROBIT window.

Note that you can load the mycobit.hex on a v2 microbit, but you will not be able to use all of the v2 features. Trying to load the v2 hex file on a microbit v1 will show a MemoryError on the display. You need to load the mycobit.hex on a microbit v1.

The yellow LED on the back of the microbit will flash while mycobit is copied and installed on your microbit.

Four things will be installed on your microbit: The micropython interpreter, the mycobit python program, a test program and a set of default programs which are identical to those built into the original MyCo/TPS boards.

When the transfer is complete, the microbit will reset and you should see an animated pattern on the display LEDs.

The animated pattern is produced by this little mycobit program which you can analyse and play with later:

43 52 43 53 41 54 7B 25 B5 10 60 71 50 A2 3E

Hint: You can change the speed of the animation by changing 25 to anything between 20 (extremely fast) and 2F (extremely slow).

Once you've got tired of watching this animation you can follow the instructions to load the Default MyCo/TPS programs below.

Learn how to use the editor to create your own programs, see First steps in the editor below.

Whenever you want to reset everything, you can simply download the hex file to your microbit, but any stored mycobit program will be overwritten with the animated pattern program.


# Manual Installation

mycobit is written in micropython, not makecode. So you'll need an editor for vanilla micro:bit micropython.

I recommend using the python mu editor as it will handle installing micropython automatically.

Load up the mycobit.py file in mu and download it to your micro:bit.

Reset your micro:bit, and let's get started with mycobit programming!

There's nothing on the display, is it dead? No, it's not dead, it's just doing nothing. You need to add a mycobit program.

# First steps in the editor

Keep button B held down and press and release the reset button.
When the micro:bit restarts four of the top leds will light up. You're in the mycobit editor!
The highlighted leds are the editor 'cursor', showing you which nibble is to be edited. Release button B and the leds will turn off.

mycobit is a 4-bit system, everything exists within groups of 4 binary digits from 0000 to 1111 or, in base 16 (hexadecimal), 0x0 to 0xF.
8-bit systems are based on groups of 8 binary digits, commonly called bytes. 4 bit groups are smaller than bytes and are often referred to as nibbles or nybbles.

NOTE: The latest version of mycobit uses the original MyCo/TPS editor mode. Every time you move to a new nibble with button B, the next press of button A will put a zero in the nibble. This isn't so obvious when you are working with empty memory which is already all zeroes. Some versions of mycobit, including the versions for different boards, just added one to the value already in the nibble. If the following instructions don't seem to work, you are probably using an older version. Just press button A until you get the value you want!

Press and release button A until one led is displayed in the top right-hand corner of the display. The value 1 is now in the first nibble.
Hold button A down and it will cycle through all 16 values. Some action!

Pressing button B will move to the next nibble, it will be highlighted with the cursor.
Hold down button B and it will move through the mycobit memory.
Note: You cannot move backwards in memory, you've only got buttons A, B and reset!
If you go too far in the memory you'll need to save your current program and then reset to get back to the start of memory. Don't worry it's not difficult, see below. You'll get used to it.

As the cursor moves through the memory you'll see some leds light up on the left and bottom of the display. These indicate the byte address in mycobit memory.
The left column indicates the byte you are editing. The display shows two bytes, split into four nibbles. So two of the nibbles have the same byte address.
The bottom row indicates which page you are editing. mycobit memory is split into 16 bytes in 16 pages. Address space of 256 bytes, think of all the possibilities!

The overall editor display looks like this:

``b . . . .`` <br/>
``y . . . .`` <br/>
``t . . . .`` <br/>
``e . . . .`` <br/>
``. e g a p`` <br/>

'egap' is page backwards, simply because the pages are counted on the display from right to left to match the way nibble values are displayed!

The left column will count from 0 to 15 (top to bottom), depending on the byte being edited.
The bottom row will count from 0 to 15 (right to left - to match the nibble values), depending on the page.
You'll get used to it!

# First Program Tutorial

Reset the micro:bit with button B held down to get back into the editor at byte 0.

Instructions go in the first nibble of each byte.

Repeatedly press button A until the value 1 is shown on the top row of leds: ``. . . . O``

The instruction 1 shows a value on the display at runtime.

Press button B (don't hold) to highlight the second nibble.

Data values go in the second nibble of each byte.

For instruction 1, the data will be the value shown on the mycobit display.

Press button A until the value 10 (0x0A) is displayed: ``. O . O .``

Hold down button A to step through all the values, if you go too far, just cycle around again until you get back to be value that you need.
 
The second instruction will be a relative jump to itself to 'stop' the program.

Press button B to highlight the third row of leds, the top left led lights up, you are editing byte 1.

Repeatedly press button A until the value 3 is displayed: ``. . . O O``

Press button B to highlight the fourth row of leds.

If the memory was empty when you started then this already shows zero, if not cycle around with button A to zero (no leds lit).

Now your complete micro:bit display should look like this (including the memory counters):

``o . . . O`` <br/>
``. O . O .`` <br/>
``. . . O O`` <br/>
``. . . . .`` <br/>
``. . . . .`` <br/>

Note that the memory counters are shown dimmer than the contents of memory.

# Saving and running that first program

You've got a program in the editor, but now you need to run it.
First, you need to save that program to the micro:bit flash.
Hold down button B. The editor will start scrolling through memory. This is ok, you are only viewing and moving the cursor, not editing.
While keeping button B held down, also hold down button A until the display clears.

The program has now been saved in the micro:bit.

Release both buttons.

If everything worked correctly the stored program will run and you'll see the value 10 (0x0A) displayed on the lop row of leds: ``. O . O .``

Wow, amazing, it worked!

# Running a stored program

To run a stored program, just turn on the micro:bit without any buttons pressed and the program will run, that's it!

If you click the reset button on the back of micro:bit without any buttons pressed, the saved program will also run.

# Editing a saved program

To edit a saved program, just reset the micro:bit with button B held down. Release button B when you see the display.
You're now in the editor which shows your stored program.

Enjoy!

# Example Program - simple binary counter

Here's a very simple little example program just to give you a taste of programming mycobit with a bit more action.
It will show a binary counter on the top row of the display. Don't worry about understanding the commands, just get used to pressing the correct buttons at the right time to control the editor.

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

The complete mycobit instruction set is described in [Instruction set.](https://github.com/veryalien/mycobit/blob/master/doc/Instruction_set.md "Instruction Set")

A table of all the instructions and all of the micro:bit pin mappings can be found in [mycobit info.](https://github.com/veryalien/mycobit/blob/master/doc/mycobit_info.pdf "mycobit_info")

# Default MyCo/TPS programs

Note: To make full use of the default demo programs you will need some kind of breakout board (bob) for your bit, so you can access all of the relevant pins on the edge connector. Without any breakout board you'll just see some blinking leds as that is the default MyCo/TPS demo without any input pins set to the correct state. The default program can be easily modified to allow most of the demo programs to work without any connected hardware, follow these instructions for [default programs without a bob](https://github.com/veryalien/mycobit/blob/master/doc/Default_no_bob.md "Default no bob").

The original MyCo/TPS system came with a default set of built-in demo programs and subroutines.
You can find exactly the same mycobit programs here in the file called 'default'.

These demos contain the following programs:

1 - Binary counter. This shows a counter on the top row of the display from 0 to F (15, binary 1111). The analogue output PWM is also changed on micro:bit pin 0, but this is not shown on the display.

2 - Analogue input. This reads the value of AD1 (Analogue to digital 1 - micro:bit pin 1) and displays the corresponding digital value on the top row of the display. Without any input on micro:bit pin 1, this will probably show 3 on the display ``.  .  .  O  O``

4 - 'Random' number generator. When started this will first show B (11, binary 1011) on the display. This isn't really a random number generator, while button A is held down, the top row very quickly cycles through 0 to F. So you cannot really see the value. When you release button A, the display will stop at whatever 'random' number it was at in the sequence. By the way, 0 is a valid number, so if you manage to stop at 0, no leds will be lit. You didn't break it, just hold button A again!

8 - Stopwatch. When started the display will be empty. When button A is held down a fast counter (but not as fast as the random number) will begin from 0 and keep cycling. When button A is released the display shows the current value. You can pick a number from 0 to 15 and keep trying to stop the stopwatch on that value!

C - Stopwatch with two buttons. When started the display will be empty. When button A is held down a fast counter (but not as fast as the random number) will begin from 0 and keep cycling. When you release button A the stopwatch does not stop! Press button B and the stopwatch will stop and show the current value. You must press button B again to reset the stopwatch. The display will now be empty and the stopwatch can be restarted by pressing button A again. If you manage to hit button B on 0, you'll still have to reset the stopwatch by pressing button B again, otherwise it will not restart when you press button A. There's another little mycobit game for you, try to stop the stopwatch exactly on 0!

The demo program numbers 1, 2, 4, 8 and C are the digital input pin values that need to be read at reset to start the relevant demo program. 

MyCo/TPS has a nifty way to get back to a known default state by re-loading the original demo programs from a hidden part of memory.
This behaviour is also implemented in mycobit, but first you'll need to copy the 'default' file to the micro:bit.
The easiest way is to get the 'default' file from the mycobit github repository and copy it to your mu-code directory.

Use the mu files tab to show the files on your micro:bit. On the left you'll see the list of files on your micro:bit, with mycobit installed probably just mycobit programs you might have saved. Programs are saved and loaded to and from the micro:bit micropython file system via a file called 'mycobit'.

On the right side, mu will show the list of files on your computer, if you've copied 'default' to your mu-code directory it will appear here.

Drag the 'default' file onto the micro:bit file list. It will be copied over to the micro:bit. You only have to do this once, or after you've been using your micro:bit for other things, or perhaps modifying the mycobit python program, and the micropython file system got re-flashed.

Now you can use the editor to load the default mycobit programs whenever you want, this will however completely overwrite any stored programs in the file 'mycobit'.

Reloading the default programs is as simple as going into the editor and setting the first four nibbles of memory to 15 (0x0F). Go into the mycobit editor and set everything to 1 bits using buttons A and B, it will end up looking like this:

``o O O O O`` <br/>
``. O O O O`` <br/>
``. O O O O`` <br/>
``. O O O O`` <br/>
``. . . . .`` <br/>

Now press and hold button B, while holding press button A. This will save 0xFF 0xFF as a program, but when this is reloaded mycobit will see it as the magic reset number. 0xFF 0xFF can never occur as the first two bytes in a real mycobit program.

mycobit will now load the default programs from the file 'default' into the 'mycobit' file. You've 'lost' your program, but now you've got the demo programs loaded - more details on using the demos coming soon!

If you see the top row left and right pixels blinking then it's working!

If you go into the editor (reset with button B pressed) you'll now see the first four nibbles of the demo program instead of 0xF 0xF 0xF 0xF.

``. . O O .`` <br/>
``. . O . .`` <br/>
``. . O . O`` <br/>
``. . . . O`` <br/>
``. . . . .`` <br/>

6 - A= ... <br/>
4 - Din - read the digital input pins (to select the relevant demo)

5 - move the contents of register A to ... <br/>
1 - register B

You can now continue using mycobit as before, you can browse through the demo programs and try to work out what they do. Read the MyCo documents which explains them in detail. Otherwise you can just go into the editor and overwrite the demo program code with your own.

If you ever need to get back to a known state just follow these instructions again and the default programs will be re-loaded.


# Can mycobit use the edge connector pins on the micro:bit?

It can and it does, both analogue and digital inputs and outputs are supported. Check the info sheet for more details.

# How do I make a bob for my bit?

You can make a relatively simple, but useful breakout board to use with mycobit using a breadboard and some basic, easy to obtain hobby electronics components.

To use all of the mycobit input and output commands and pins, you will need access to the following edge connector pins:

Pin  0 - PWM - analogue output using Pulse Width Modulation.

Pin  1 - AD1 - analogue input 1 or Dout pin 3 digital output

Pin  2 - AD2 - analogue input 2 or Dout pin 2 digital output

Note: Pins 1 and 2 cannot be used for both input and output in the same program

Pin  8 - Dout pin 1 digital output

Pin 12 - Dout pin 0 digital output - originally intended for micro:bit 'accessibility' features and some breakouts don't break out pin 12

Pin 13 - Din pin 3 - digital input

Pin 14 - Din pin 2 - digital input

Pin 15 - Din pin 1 - digital input

Pin 16 - Din pin 0 - digital input


Any breakout board that you use must give access to the relevant pin, otherwise using the corresponding mycobit commands will have no effect.

A few connections will be needed to inputs (switches, potentiometers, analogue sensors, etc.) and outputs (buzzers, LEDs, etc,) - coming soon!


# mycobit History

For a complete guide to MyCo/TPS you can have a look at the german site: http://www.elektronik-labor.de/Lernpakete/TPS/TPS0.html

At that site you'll see that TPS has a long history, going back over a number of years.

I bought this [Microcontroller Pack](https://www.conrad.com/p/conrad-components-10104-profi-mikrocontroller-course-material-14-years-and-over-192286 "Conrad TPS Pack") from Conrad and I was hooked.

I apolgise profusely for the state of the 'denglisch' on the Conrad page, it might be actually be 'double Dutch', but never mind!

I've lived in Germany for over 20 years, so it's not that much of a problem for me to understand the original documentation.

For a lot of useful information in english I suggest that you download this pdf: http://www.elektronik-labor.de/Literatur/MyCo2014.pdf

That is a free excerpt from a complete instruction manual which you can still purchase from amazon.
Please note though that, unfortunately, the instruction table is very strangely formatted and doesn't contain all of the proper instruction descriptions. See the mycobit_info.pdf file for more details.

mycobit is fully backwards-compatible with the MyCo/TPS systems. There are a few enhancements that add new extended commands, support the larger micro:bit display and available memory. The input and output pins have been assigned according to the micro:bit edge connector analogue and digital pins. See the limitations section for all the annoying limiting features and issues.

# mycobit Versions

Here is a list of all the mycobit versions. All are more or less up and running, not all of them are currently released. Watch this space.

The names keep changing. I might change from myco: my (little) computer, into mycro: my (little) microprocessor. I don't think I'm infringing any copyright by using ':'. So, in the future, you might see mycro:bit, mycro:bpi, mycro:nano, mycro:meow, etc.

In a strange quirk of fate, mycobit has so far been implemented for 4 bits!! (and perhaps a few more bits...)

### myco:bit

mycobit is for the micro:bit. This version of mycobit!

### myco:bpi

mycobpibit is for the banana pi bpi:bit The bpi:bit uses an esp32 and there is simply more free runtime memory available for micropython. The bpi:bit also has an RGB 5x5 LED display which is very nice indeed. mycobpibit includes additional display colour commands!

### myco:nano

myconanobit is for the kittenbot nanobit, a micro:bit with a Arduino nano pin layout, and no built-in LED matrix display (but with the row pins, so you could make your own display on a bob). The nanobit is unfortunately a bit difficult to order from outside asia. Documentation and support are very tricky. A couple of strange limitations based on memory usage versus mycobit. But it all works!

### myco:meow

myco:meow (maybe I'll change all the names before release?!) is for the kittenbot meowbit, a makecode arcade board, with a large colour screen and arcade type controls. It has a micro:bit compatible edge connector. Adafruit circuitpython will probably be used on the STM32 instead of micropython. However, I'm currently sticking with the kittenbot meowbit micropython implementation. Circuitpython is just too different to micropython to easily convert all the code in one swoop, and the file system has different read/write protection, so that's a bit tricky.
  
The meowbit has a really interesting wireless SD card add-on which is effectively a micro:bit in an SD card format for meowbit to micro:bit compatible radio and bluetooth communication. This add-on card is difficult to order outside asia. Wireless is not used by mycobit, but nice anyway.

### myco:clue

The 5th 'bit'! I'll see what I can do with a proper circuitpython version, which will probably feed back into the pre-release meowbit version too.

### myco:stack, myco:stick, myco:atom

Implementations for the M5Stack range of ESP32 devices, each with their own particular I/O components.

# Limitations (mostly on microbit v1)

The '4 bit' mycobit implementation was strictly observed, the micro:bit display is not used with the built-in display features to scroll messages and show images. Only the top-right hand 4 x 4 pixels are used as a display, but it is still very useful. Light-sensing, via the display leds, is not available.

No SPI or I2C devices are supported. The SPI pins have been used as GPIO pins. I2C cannot be used on the microbit v1 due to space limitations.

Unfortunately micropython on the micro:bit v1's nrf51822 doesn't leave much memory free and it was a struggle to get the latest mycobit.py to be loaded successfully without any memory errors. The source has virtually no comments and lots of pretty whitespace and variable names have been manually omitted, minifying the source didn't make any difference any more.

There are a couple of enhanced shift and rotate instructions in the latest version of the code. But, unfortunately, any further addtions, or even subtle changes to the python code, seem to make the python too large or complex for it to be successfully compiled to byte-code when loaded. If you want to play with the mycobit python source code for your own programs, you can switch things 'on' and 'off' by carefully commenting them out in the mu-editor and then re-loading the modified mycobit.py onto the micro:bit. 


