# 02 Wait

# Instruction 2

This example displays different values on the mycobit display waiting between each value

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
|  0     |  8     |  3     |  0     |  HALT - jump backwards 0 bytes, so that the program stops|


Change the wait data values to different values between 0 (hexadecimal 0x0, binary 0000) and 15 (hexadecimal 0xF, binary 1111) to change the delay between displaying each value.
