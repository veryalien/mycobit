# Default programs without a bob

The original default programs were designed to be used with the MyCo and TPS hardware boards that are connected to hardware input/output pins.

When the board is restarted the main default program first looks for which demo has been selected on the Din hardware pins.

If the program doesn't see any of the pins have been 'set' at reset, actually by pulling the pins down to ground, it just blinks the top left and right leds in a 'waiting for input' indication.

The blinking leds are all you'll ever see with mycobit without a connected bob. But the program can easily be changed to simulate the hardware pins being set.

Make sure you've followed the instructions to get mycobit installed and running with the default file copied to your micro:bit.

If everything has been done correctly, after a reset you'll just see the top leds blinking alternately <br/>
``.  .  .  .  O`` followed by <br/>
``.  O  .  .  .``

The demo program numbers 1, 2, 4, 8 and C are the digital input pin values that need to be read at reset to start the relevant demo program. To make things just a little more complicated, the digital input states are inverted through pullup resistors. The actual values needed are the inverted values, or 15 - the original value: E (14, 1110), D (13, 1101), B (11, 1011), 7 (0111) and 3 (0011).

This change simulates pulling the input pins down to ground to change the value read at reset.

To edit the default program:

You only need to change the first command from 64 to 4x, the values are as follows to start each different program after reset:

4E - Binary counter.

4D - Analogue input - is still no use without anything connected as an analogue input to micro:bit pin 1.

4B - 'Random' number generator.

47 - Stopwatch.

43 - Stopwatch with two buttons.

Remember to save your change by holding down button B and then holding down button A until the display clears.

The demo program you've selected will then be run.

If you accidentally (or deliberately!) enter other values for selecting a demo program, you'll just see the top left and right leds blinking alternately. If you see that, you've probably done something wrong, so check your first command again in the editor.
 

