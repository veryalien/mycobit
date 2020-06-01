# mycobit
A 4-bit computer system for the microbit.

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

Press and release button A again and one led  will be displayed in the top right-hand corner of the display. Now the value one is in the first nibble.
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

Press button A twice so the value 1 is shown on the top row of leds: . . . . O
The first press puts zero in the nibble, which you obviously can't see.
The instruction 1 shows a value on the display at runtime.

Press button B (don't hold) to highlight the second nibble.

Data values go in the second nibble of each byte.
For instruction 1, the data will be the value displayed.

Press button A until the value 10 (0x0A) is displayed: . O . O .
That will be 11 individual presses - including zero at the start.
 
The second instruction will be a relative jump to itself to 'stop' the program.

Press button B to highlight the third row of leds, the top left led lights up, we are editing byte 1.

Press button A until the value 3 is displayed: . . . X X

Press button B to highlight the fourth row of leds.

Press button A once, not really needed when the memory is empty, but this puts zero into the nibble.

Now your complete microbit display should look like this (including the memory counters):

o . . . O <br/>
. O . O . <br/>
. . . O O <br/>
. . . . . <br/>
. . . . . <br/>

Note that the memory counters are shown dimmer than the contents of memory.

The overall editor display looks like this:

b . . . . <br/>
y . . . . <br/>
t . . . . <br/>
e . . . . <br/>
. e g a p <br/>

egap is page backwards as we count the bytes from right to left!


# Saving and Running that first program!

We've got a program in the editor, but now we need to run it.
First, you need to save that program to the microbit flash.
Hold down button B. The editor will start scrolling through memory. This is ok, we are only viewing not editing.
While holding down button B, hold down button A until the display clears.
The program has now been saved in the microbit.
Release both buttons.

If everything worked correctly you'll see the value 10 (0x0A) displayed on the lop row of leds: . O . O .

Wow, amazing, it worked!

# Running a stored program

To run a stored program, just turn on the microbit and the program will run, that's it!

If you click the reset button on the back of microbit without any buttons pressed, the saved program will also run.

# Editing a saved program

To edit a saved program, just reset the microbit with button B held down. Release the button when you see the display.
You're now in the editor which shows your stored program.

Enjoy!

# What do all those mycobit instructions do?

Good question, more info coming soon!

# Can mycobit use the edge connector pins on the microbit?

It can and it does both analogue and digital inputs and outputs are supported. 

