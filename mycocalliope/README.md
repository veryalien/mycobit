# mycocalliope - ALPHA

A 4-bit computer system for the Calliope.

Mycocalliope is an implementation of the MyCo (My little Computer) system, also known in german as TPS (Tastenprogrammierbare Steuerung).

You can create, save and run useful programs directly on the Calliope, without needing a computer connected at all.
Once mycocalliope has been installed on the Calliope you can program using only the three buttons A, B and reset!

# Getting Started

A quick start-up guide to getting mycocalliope running on your Calliope.

# Easy Installation

Connect your Calliope to your computer and you should see a device window called MINI.
 
Download the file mycocalliope.hex and copy it to your Calliope by dragging the file into the MINI window.

The yellow LED on the front of the Calliope will flash while mycocalliope is copied and installed.

Two things will be installed on your Calliope: The micropython interpreter and the mycocalliope micropython program.

When the transfer is complete, the microbit will reset and (in the ALPHA version) you will see nothing at all!

See First steps in the editor below.


# Manual Installation

Copy mycocalliope.py to the Calliope using the micropython utilities. Instructions coming soon (if needed).

# First steps in the editor

Keep button B held down and press and release the reset button.
When the Calliope fully restarts (it takes a good 8 seconds - keep button B pressed) four of the top leds will light up. You're in the mycocalliope editor!
The highlighted leds are the editor 'cursor', showing you which nibble is to be edited. Release button B and the leds will turn off.

mycocalliope is a 4-bit system, everything exists within groups of 4 binary digits from 0000 to 1111 or, in base 16 (hexadecimal), 0x0 to 0xF.
8-bit systems are based on groups of 8 binary digits, commonly called bytes. 4 bit groups are smaller than bytes and are often referred to as nibbles or nybbles.

Press and release button A until one led is displayed in the top right-hand corner of the display. The value 1 is now in the first nibble.
Hold button A down and it will cycle through all 16 values. Some action!

Pressing button B will move to the next nibble, it will be highlighted with the cursor.
Hold down button B and it will move through the mycocalliope memory.
Note: You cannot move backwards in memory, you've only got buttons A, B and reset!
If you go too far in the memory you'll need to save your current program and then reset to get back to the start of memory. Don't worry it's not difficult, see below. You'll get used to it.

As the cursor moves through the memory you'll see some leds light up on the left and bottom of the display. These indicate the byte address in mycocalliope memory.
The left column indicates the byte you are editing. The display shows two bytes, split into four nibbles. So two of the nibbles have the same byte address.
The bottom row indicates which page you are editing. mycocalliope memory is split into 16 bytes in 16 pages. Address space of 256 bytes, think of all the possibilities!

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

Reset the Callope mini with button B held down to get back into the editor at byte 0.

Instructions go in the first nibble of each byte.

Repeatedly press button A until the value 1 is shown on the top row of leds: ``. . . . O``

The instruction 1 shows a value on the display at runtime.

Press button B (don't hold) to highlight the second nibble.

Data values go in the second nibble of each byte.

For instruction 1, the data will be the value shown on the mycobitcalliope display.

Press button A until the value 10 (0x0A) is displayed: ``. O . O .``

Hold down button A to step through all the values, if you go too far, just cycle around again until you get back to be value that you need.
 
The second instruction will be a relative jump to itself to 'stop' the program.

Press button B to highlight the third row of leds, the top left led lights up, you are editing byte 1.

Repeatedly press button A until the value 3 is displayed: ``. . . O O``

Press button B to highlight the fourth row of leds.

If the memory was empty when you started then this already shows zero, if not cycle around with button A to zero (no leds lit).

Now your complete display should look like this (including the memory counters):

``o . . . O`` <br/>
``. O . O .`` <br/>
``. . . O O`` <br/>
``. . . . .`` <br/>
``. . . . .`` <br/>

Note that the memory counters are shown dimmer than the contents of memory.

# Saving and running that first program

You've got a program in the editor, but now you need to run it.
First, you need to save that program to the Calliope flash memory.
Hold down button B. The editor will start scrolling through memory. This is ok, you are only viewing and moving the cursor, not editing.
While keeping button B held down, also hold down button A until the display clears.

The program has now been saved in the Calliope.

Release both buttons.

If everything worked correctly the stored program will run and you'll see the value 10 (0x0A) displayed on the lop row of leds: ``. O . O .``

Wow, amazing, it worked!

# Running a stored program

To run a stored program, just turn on the Calliope without any buttons pressed and the program will run, that's it! It takes a few seconds for the Calliope to start after power on, or after a reset.

If you click the reset button on the Calliope without any buttons pressed, the saved program will also run.

# Editing a saved program

To edit a saved program, just reset the Calliope with button B held down. Release button B when you see the display.
You're now in the editor which shows your stored program.

Enjoy!

# Example Program - simple binary counter

Here's a very simple little example program just to give you a taste of programming mycocalliope with a bit more action.
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


# What do all those mycocalliope instructions do?

The complete mycocalliope instruction set is described in [Instruction set.](https://github.com/veryalien/mycobit/blob/master/doc/Instruction_set.md "Instruction Set") - NOT ALL OF THESE INSTRUCTIONS DO THE SAME ON THE CALLIOPE - for example the 00 and FF memory instructions are not supported and you cannot skip an instruction if a button is not pressed. More details soon!

A table of all the instructions and all of the micro:bit pin mappings can be found in [mycobit info.](https://github.com/veryalien/mycobit/blob/master/doc/mycobit_info.pdf "mycobit_info") - NOT ALL OF THESE INSTRUCTIONS DO THE SAME ON THE CALLIOPE - see above.

# Default MyCo/TPS programs

The default programs are not supplied with the mycocalliope ALPHA!

# Can mycocalliope use the I/O pads and pins like on the micro:bit?

It can and it does, both analogue and digital inputs and outputs are supported. The ALPHA version supports only the following:

Pad 0 - analogue output

Pad 1 - analogue input

Pad 2 - digital input

Pad 3 - digital output

# How do I make a bob for my Calliope?

Coming soon?!

# mycobit History

See the mycobit pages


