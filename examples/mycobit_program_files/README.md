# mycobit program files

These pre-defined program files allow you to use different mycobit programs without using the (annoying?) editor and the micro:bit buttons.

Pre-defined mycobit program files are binary data files without any 'dot' file type. They are not python or hex files, please do not use any dot file type in the file name. 

Download and copy a pre-defined mycobit program file to your mu-code folder and rename the file to exactly the name: mycobit

Open the mu-editor.

Connect a micro:bit, with the mycobit system already installed (see the main README file for setup details).

Open the mu files tab.

Drag the mycobit file from the 'Files on your computer:' list to the 'Files on your micro:bit:' list.

If there is already a file called mycobit, agree that you want to overwrite the file.

The file should be successfully copied.

Reset the micro:bit and the pre-defined mycobit program will run.

You can reset the micro:bit with button B held down to start the editor if you want to look at the mycobit program commands.

# List of pre-defined program files

### mycobit_show_font

Displays all 64 pre-defined characters stored in Pages 0x08 to 0x0F of the 'default' program file.
The original TPS system only used 8 memory pages and the default programs could omly use those 8 pages. mycobit provides 16 memory pages which is enough space to define 64 4x4 characters which could be used on the mycobit display.
