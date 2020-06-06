# 01 Display Value

# Instruction 1

This example displays a binary value on the mycobit display using instruction 1


|  Page  |  Byte  |  Inst  |  Data  |  Comments  |
|  ---   |  ---   |  ---   |  ---   |  ---    |       
|  0     |  0     |  1     |  1     |  Show the data value 1 on the mycobit display ``. . . . O`` |
|  0     |  1     |  3     |  0     |  HALT - jump backwards 0 bytes, so that the program stops   |


Change the data value to any value between 0 (hexadecimal 0x0, binary 0000) and 15 (hexadecimal 0xF, binary 1111) to show the binary value on the mycobit display.
