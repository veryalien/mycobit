# mycobit Instruction Set Summary

Brief "cheat sheet" details for the complete mycobit instruction set.

Command bytes have an instruction high nibble and a data low nibble. When entering commands in the editor the high nibble is shown first with the low nibble underneath.

For example the commands 41 54 would be shown in the editor as:

`` o . O . .`` <br/>
`` . . . . O`` <br/>
`` . . O . O`` <br/>
`` . . O . .`` <br/>
`` . . . . .`` <br/>


|  Inst |  Data    | Name                 | Notes  |
|  ---  |  ---     |  ---                 | ---    |
|  0    |  0       | get lnib             | Read the low nibble value from the memory address: C (Page) + B (Byte) |
|  0    |  1       | set lnib             | Write the low nibble to the memory address: C (Page + B (Byte) |
|  1    |  0...F   | Disp.Row=            | Show the data value on the currently selected row of the display |
|  2    |  0...F   | Wait                 | Wait for the data delay time (delay from 0 = 1ms to F = 60s)|
|  3    |  0...F   | Jump back            | Relative jump backwards of data bytes |
|  4    |  0...F   | A=                   | Set register A to data value |
|  5    |  0       | Row=A                | Select the display row from register A, which should be a value between 0 and 3 |
|  5    |  1       | B=A                  | Set register B to register A |
|  5    |  2       | C=A                  | Set register C to register A |
|  5    |  3       | D=A                  | Set register D to register A |
|  5    |  4       | Disp.Row=A           | Set display Row to register A |
|  5    |  5       | Disp.Row.0=A.0       | Set Bit 0 of display Row to the lowest bit of register A |
|  5    |  6       | Disp.Row.1=A.0       | Set Bit 1 of display Row to the lowest bit of register A |
|  5    |  7       | Disp.Row.2=A.0       | Set Bit 2 of display Row to the lowest bit of register A |
|  5    |  8       | Disp.Row.3=A.0       | Set Bit 3 of display Row to the lowest bit of register A |
|  5    |  9       | PWM=A                | Set the PWM (Pulse Width Modulation) analogue output (micro:bit pin 0) to register A |
|  5    |  A       | Dout=A               | Set the digital outputs (micro:bit pins 1, 2, 8 and 12) to register A |
|  5    |  B       | Dout.0=A.0           | Set Dout.0 (micro:bit pin 12) to the lowest bit of register A | 
|  5    |  C       | Dout.1=A.0           | Set Dout.1 (micro:bit pin 8) to the lowest bit of register A | 
|  5    |  D       | Dout.2=A.0           | Set Dout.2 (micro:bit pin 2) to the lowest bit of register A | 
|  5    |  E       | Dout.3=A.0           | Set Dout.3 (micro:bit pin 1) to the lowest bit of register A | 
|  6    |  0       | A=Row                | Set register A to the currently selected display row |
|  6    |  1       | A=B                  | Set register A to register B |
|  6    |  2       | A=C                  | Set register A to register C |
|  6    |  3       | A=D                  | Set register A to register D |
|  6    |  4       | A=Dout               | Set register A to the digital outputs (micro:bit pins 1, 2, 8 and 12) |
|  6    |  5       | A=Dout.0             | Set register A to Dout.0 (micro:bit pin 12) | 
|  6    |  6       | A=Dout.1             | Set register A to Dout.1 (micro:bit pin 8) | 
|  6    |  7       | A=Dout.2             | Set register A to Dout.2 (micro:bit pin 2) | 
|  6    |  8       | A=Dout.3             | Set register A to Dout.3 (micro:bit pin 1) |
|  6    |  9       | A=AD1                | Set register A to AD1 (Analogue to Digital 1 - micro:bit pin 1) |
|  6    |  A       | A=AD2                | Set register A to AD2 (Analogue to Digital 2 - micro:bit pin 2) |
|  6    |  F       | Save memory          | Save the entire contents of memory to the 'mycobit' file |
|  7    |  1       | A=A+1                | Add 1 to register A |
|  7    |  2       | A=A-1                | Subtract 1 from register A |
|  7    |  3       | A=A+B                | Add register B to register A |
|  7    |  4       | A=A-B                | Subtract register B from register A |
|  7    |  5       | A=A*B                | Multiply register A by register B |
|  7    |  6       | A=A/B                | Divide register A by register B |
|  7    |  7       | A=A and B            | Logically AND the bit values of register A and register B |
|  7    |  8       | A=A or B             | Logically OR the bits values of register A and register B |
|  7    |  9       | A=A xor B            | Logically XOR (exclusive or) the bit values of register A and register B |
|  7    |  A       | A=not A              | Logically invert all the bit values of register A |
|  7    |  B       | A=A&lt;&lt;1         | Shift register A left |
|  7    |  C       | A=A&gt;&gt;1         | Shift register A right |
|  7    |  D       | A=A rot&lt;&lt;1     | Rotate register A left |
|  7    |  E       | A=A rot&gt;&gt;1     | Rotate register A right |
|  8    |  0...F   | Select Page          | Select memory Page - blocks of 16 bytes |
|  9    |  0...F   | Jump                 | Jump to the byte at position data in the selected memory page |
|  A    |  0...F   | DCJNZ                | If C is not zero, decrement C and jump to the byte at position data in the selected memory page |
|  B    |  0...F   | DDJNZ                | If D is not zero, decrement D and jump to the byte at position data in the selected memory page |
|  C    |  -       | -                    | Skip next instruction ... |
|  C    |  0       | A==0                 | ... if register A is equal to 0 |
|  C    |  1       | A>B                  | ... if register A is greater than register B |
|  C    |  2       | A&lt;B               | ... if register A is less than register B |
|  C    |  3       | A==B                 | ... if register A is equal to register B |
|  C    |  4       | Din.0==1             | ... if Din.0 (micro:bit pin 16) is high <br/>Note: pullup resistors invert all Din pin states!|
|  C    |  5       | Din.1==1             | ... if Din.1 (micro:bit pin 15) is high |
|  C    |  6       | Din.2==1             | ... if Din.2 (micro:bit pin 14) is high |
|  C    |  7       | Din.3==1             | ... if Din.3 (micro:bit pin 13) is high |
|  C    |  8       | Din.0==0             | ... if Din.0 (micro:bit pin 16) is low |
|  C    |  9       | Din.1==0             | ... if Din.1 (micro:bit pin 15) is low |
|  C    |  A       | Din.2==0             | ... if Din.2 (micro:bit pin 14) is low |
|  C    |  B       | Din.3==0             | ... if Din.3 (micro:bit pin 13) is low |
|  C    |  C       | S1==0                | ... if S1 (micro:bit button A) is not pressed |
|  C    |  D       | S1==0                | ... if S2 (micro:bit button B) is not pressed |
|  C    |  E       | S1==1                | ... if S1 (micro:bit button A) is pressed |
|  C    |  F       | S1==1                | ... if S2 (micro:bit button A) is pressed |
|  D    |  0...F   | Call                 | Call subroutine at byte position data in the selected memory page <br/>Note: No nested subroutines allowed!|
|  E    |  0       | Ret                  | Return from subroutine call |
|  F    |  0       | get hnib             | Read the high nibble value from the memory address: C (Page) + B (Byte) |
|  F    |  1       | set hnib             | Write the high nibble to the memory address: C (Page + B (Byte) |

