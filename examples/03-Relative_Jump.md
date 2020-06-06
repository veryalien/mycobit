# 03 Wait

# Instruction 3

This example uses a relative loop instruction to jump backwards in the program

|  Page  |  Byte  |  Inst  |  Data  |  Comments  |
|  ---   |  ---   |  ---   |  ---   |  ---    |   
|  0     |  0     |  1     |  1     |  Display data value 1 ``. . . . O`` |
|  0     |  1     |  2     |  8     |  Wait for 500ms (0.5 seconds)  |
|  0     |  2     |  1     |  2     |  Display data value 2 ``. . . O .`` |
|  0     |  3     |  2     |  8     |  Wait 500ms |
|  0     |  4     |  1     |  4     |  Display data value 4 ``. . O . .`` |
|  0     |  5     |  2     |  8     |  Wait 500ms |
|  0     |  6     |  1     |  8     |  Display data value 8 ``. O . . .`` |
|  0     |  7     |  2     |  8     |  Wait 500ms |
|  0     |  8     |  3     |  8     |  Jump backwards 8 bytes to byte 0, the program will loop forever|

Change the jump data value in byte 7 to 2 or 4 so that the repeated pattern on the display is different.

From the other examples, setting a relative jump backwards of 0 is a good way to halt a mycobit program.
