# hackAssembler
An assembler for the Hack assembly language used in Nand2Tetris I 

This project is a python implementation of a Hack Assembler. It converts code written in Hack assembly (.asm) to machine code i.e. binary form (.hack)

To run the script, the assembly code should be in the same directory as the script. Then the script is executed as follows from the command line

![comm](https://user-images.githubusercontent.com/73723384/158030736-63215e27-6ba7-4087-91db-a9de3a9bff3b.PNG)

The output file is automatically saved to the same directory and its extension is .hack

The functions of the individual scripts
  
  Cleaner.py  : This removes comments and blank spaces in the code. It also replaces all labels and variables used in the code with their respective addresses.
  
  Parser.py   : This gets the individual sections of c instructions i.e destination, computation and the jump
  
  Code.py     : This gives the binary equivalent for destination, computation or jump using its functions
  
  Assembler.py: This uses all the scripts above to do the final translation to binary for both a and c instructions. 
