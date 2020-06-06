# 05 Display Row

# Instructions 4, 5 and 6

This example uses the instructions 4, 5 and 6 to control the mycobit display and light each of the pixels individually.

|  Page  |  Byte  |  Inst  |  Data  |  Comments  |
|  ---   |  ---   |  ---   |  ---   |  ---    |   
|  0     |  0     |  4     |  0     |  Set register A to the value 0 |
|  0     |  1     |  5     |  0     |  Set register Row to the value of register A |
|  0     |  2     |  4     |  1     |  Set register A to the value 1 |
|  0     |  3     |  5     |  5     |  Set Disp.Row.0 to the value of register A ``. . . . O`` | 
|  0     |  4     |  2     |  8     |  Wait for 500ms (0.5 seconds)  |
|  0     |  5     |  5     |  6     |  Set Disp.Row.1 to the value of register A ``. . . O .`` | 
|  0     |  6     |  2     |  8     |  Wait for 500ms (0.5 seconds)  |
|  0     |  7     |  5     |  7     |  Set Disp.Row.2 to the value of register A ``. . O . .`` | 
|  0     |  8     |  2     |  8     |  Wait for 500ms (0.5 seconds)  |
|  0     |  9     |  5     |  8     |  Set Disp.Row.3 to the value of register A ``. O . . .`` | 
|  0     | A (10) |  2     |  8     |  Wait for 500ms (0.5 seconds)  |
|  0     | B (11) |  6     |  0     |  Set register A to the value of register Row |
|  0     | C (12) |  7     |  1     |  A = A + 1 |
|  0     | D (13) |  3     |  C     |  Jump backwards 12 bytes to byte 1 |

