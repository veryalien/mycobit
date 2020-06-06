# 04 A = Value

# Instruction 4

This example uses instruction 4 to set register A to a specific data value.
Command 54 is also used to show the value of register A on the display, otherwise you would not see anything.
On the display, this example looks exactly like example 03-Relative_Jump, but the way it works is different.
Here a value from a register is used, not a specific 'immediate' display value.

Microcontroller registers are specific hardware addresses which are used to store variable values.
You can use them as pre-named variables in your program.

|  Page  |  Byte  |  Inst  |  Data  |  Comments  |
|  ---   |  ---   |  ---   |  ---   |  ---    |   
|  0     |  0     |  4     |  1     |  Set register A to the value 1 |
|  0     |  1     |  5     |  4     |  Set the display to the value of register A ``. . . . O`` | 
|  0     |  2     |  2     |  8     |  Wait for 500ms (0.5 seconds)  |
|  0     |  3     |  4     |  2     |  Set register A to the value 2 |
|  0     |  4     |  5     |  4     |  Display register A ``. . . O .`` |
|  0     |  5     |  2     |  8     |  Wait 500ms |
|  0     |  6     |  4     |  4     |  Set register A to the value 4 |
|  0     |  7     |  5     |  4     |  Display register A ``. . O . .`` |
|  0     |  8     |  2     |  8     |  Wait 500ms |
|  0     |  9     |  4     |  8     |  Set register A to the value 8 |
|  0     | A (10) |  5     |  4     |  Display register A ``. O . . .`` |
|  0     | B (11) |  2     |  8     |  Wait 500ms |
|  0     | C (12) |  3     |  C     |  Jump backwards 12 bytes to byte 0, the program will loop forever|

Change the values that are used for register A and see the difference on the display.

