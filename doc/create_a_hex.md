# How to create hex files for your mycobit programs 


Typing in long mycobit programs on the built-in buttons might get tedious and annoying. The TPS/SPS Emulator allows you to create, edit, run and simulate inputs and outputs before saving the program on the actual hardware board.

These step-by-step instructions will let you create a complete hex file to upload which includes everything to run mycobit programs on a microbit v1.

Note: This is the first version of the instructions and it is a bit hacky because the tools cannot currently work together automatically. The following sequence of manual steps should work, if not please let me know.


# What you will need


# TPS/SPS Emulator


Download the latest windows TPS/SPS Emulator from here: https://wkla.no-ip.biz/ArduinoWiki/doku.php?id=en:arduino:arduinosps:spsemu

If the server is up and running (unfortuantely not all the time), you should be able to download and, on windows, the program can be run directly.

You might get a virus warning about the emulator executable, which seems to be a false positive warning!
 
If you have are using Linux try installing wine and running the emulator with the command: wine SPS_Emu.exe


# micro:bit micropython editor


You will need to use the official micro:bit micropython editor in your browser to create the hex file for to your micro:bit: https://python.microbit.org


# mycobit hex file


Download the latest mycobit.hex file from github: https://github.com/veryalien/mycobit


You will replace the mycobit program embedded in this hex file with your program by following the steps below.


# Step-by-Step


# Create a program in the emulator

First, use the TPS/SPS Emulator to create your mycobit program. Set the target to BBC micro:bit. Be careful to use the correct instruction set for the original mycobit. You can manually type in the instruction and data values you want for each byte in your program. Some of the instruction decriptions in the emulator will not match with mycobit. This doesn't matter, just make sure you have the correct instructions you want to execute in your mycobit program for micro:bit v1.

Please currently avoid using any NOP instructions with 00 bytes within the program, there is a small compatibility problem with mycobit. Use a relative jump instruction like 30 to stop the program at the end if needed, or jump to the appripriate place in memory for a loop. 00 bytes after the program don't matter as long as they are never executed by mycobit.


An example would be to enter the following four instructions: 54, 29, 71, 33 into the emulator. For these instructions, the decriptions in the emulator will match correctly. This creates an endless binary counter loop which ticks every second on the outputs. Run the program in the emulator to check it works correctly. In mycobit this will display the binary counter on the micro:bit LED matrix.


Once you are happy with your program, save it as a tps file from the emulator on your computer, so you can open it again later.


# Upload to a file, not to the microbit


In the emulator click the upload button or press STRG/CTRL+U to upload the program to the target. Do not actually save it to the micro:bit, save it to a file called mycobit somewhere on your computer (remember where it is!).

 
# Create a hex containing your program


Open the micro:bit micropython editor: https://python.microbit.org


A small hello world program will be shown.


Click on the Load/Save button. A Load/Save window will open.


Drag or select your downloaded mycobit.hex file using the load area. The window will disappear and you should see the mycobit micropython program.


Click on the Load/Save button again. The Load/Save window will open with a Show Files (3) in the Project Files section. Click the Show Files button and a list of files should be shown: mycobit (main.py), default and mycobit.


Click the Add file button. A file selection window opens.


Find and open the mycobit file you saved from the emulator (not mycobit.tps, the file mycobit without any dot extension).


A message appears that says: Do you want to replace the "mycobit" file? Click on OK to replace the file.


In the Save section of the window, click Download Project Hex. A file called mycobit.hex will be downloaded through your browser to the place where you save downloaded files.


# Transfer the modified mycobit.hex to your micro:bit


Find the mycobit.hex file on your computer that you just downloaded. It doesn't matter what it is called. You can rename it to match what your mycobit program does.


Drag or copy/paste the hex file to your MICROBIT device.


The hex file will be copied to the micro:bit. The yellow LED on the back will flash. After a few seconds, the micro:bit will automatically reset.


Your mycobit program should now automatically start running! If you followed the instructions here with the binary counter you should see it run.


Your program is now stored in the micro:bit and you can edit, save and run it using the built-in buttons as for any other mycobit program.


Sometimes the hex file transfer doesn't work and you might see a FAIL file appear in your micro:bit. If you open it by clicking on it, it probably says that a timeout occurred. If this happens just unplug your micro:bit and wait a moment before plugging it back in. Once you see the MICROBIT device window, try copying your mycobit.hex file again. This usually works to solve this transfer problem.


# Do I have to do all this every time?


Once you've got everything set up correctly, you only need to do the following:


Use the emulator to create your mycobit masterpiece. Test it if you can. Note that input/output pins can't easily be tested.


In the emulator, upload your mycobit program to a file.


Open the micropython editor with the mycobit.hex file (the original or one you successfully modified).


Replace the mycobit file in the mycobit.hex and 'download' it to your computer.


Transfer the downloaded mycobit.hex to your micro:bit.



# Any problems?


Please let me know if there are any probelems. I have no idea if everything works on different systems than mine, probably not.
