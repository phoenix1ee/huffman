# Shun Fai Lee Lab3
# Huffman Compression - Encode and Decode

This python package is designed for encryption and decryption using huffman compression.
It employs the logic of Huffman Binary Tree to dynamically produce an encryption table and tree for the above purposes by the user supplied frequency table.

It accepted user input in the form of a text file for frequency table, file to be encrypted and decrypted and output to the user specified text file.

It can also perform optional actions, including output the processing time / encryption and decryption results statistics to output file, with the appropriate argument input. 

## How to download and run:

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m huffman -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m huffman <frequency_table_file> -e <some_file_to_encrypt> -d <some_file_to_decrypt> <some_output_file>`
   a. IE: `python -m huffman file/FreqTable.txt -e file/Msgtoencode.txt file/routput.txt`

Output of all encryption, decryption results will be written to the specified output file after processing the input file.

### huffman Usage:

```commandline
usage: __main__.py [-h] [-e E] [-d D] [-tm {True}] [-a {True}] fq_file out_file

use huffman compression to encode/decode message

positional arguments:
  fq_file     Frequency Table File Pathname
  out_file    Output File Pathname

options:
  -h, --help        show this help message and exit
  -e E              Optional, Pending encryption File Pathname
  -d D              Optional, Pending decryption File Pathname
  -tm {True,False}  Optional processing timer (default: False)
  -a {True,False}   Optional encode/decode analysis details (default: False)
```

Usage statements:

| Symbol   | Meaning                                                                                         |
|----------|-------------------------------------------------------------------------------------------------|
| [h]      | variable h is optional. It display the helper message                                           |
| [e]      | variable e is optional. It will allow the program to do encryption on the source file           |
| [d]      | variable d is optional. It will allow the program to do decryption on the source file           |
| [tm]     | variable tm is optional. It allows user to output the processing time at the end of output file |
| fq_file  | This is the path for frequency table input txt file. Required Positional argument               |
| out_file | This is the path for output txt file. Required Positional argument                              |
                                                                        |
## huffman Project Package and Layout

This project have a single module in a single package.
Here is huffman package explained.

* [huffman/](.): The parent package folder.
    * [README.md](README):
      The guide for using this converter
    * [huffman](huffman): 
      This is the *module* in this *package*.
      * [`__init__.py`](huffman/__init__.py) 
        
      * [`__main__.py`](huffman/__main__.py) 
        This file is the entrypoint to the converter when ran as a program. It handles the command line arguments and do all functions calling and output.
      * `builder.py` 
        This the scripts to read the input frequency table and produce the huffman binary tree and encryption code table.
      * `decoder.py` 
        This is the scripts to read the encoded input file and decode it by utilizing the created huffman binary tree 
      * `encoder.py` 
        This is the scripts to read the plain text input file and encode it by utilizing the created huffman code table 
      * `helper.py` 
        This contain functions to assist the creation of huffman binary tree.
      * `helper2.py` 
        This contain functions to perform validation and checking on the processed frequency table.
      * `lab3class.py` 
        This contained the self defined priority queue Class ADT "PQ" and huffman tree Class ADT "Htree" for use in the whole module.
      * `nodeclass.py` 
        This is the self defined H_node node class ADT, act as the components for the huffman binary tree.
      * `quicksort.py` 
        This is a self defined sorting function using quicksort to sort an array of nodes, tailored to work with the elements with the H_node types. It could perform two types of sorting. Parameter "huff" will toggle it to perform huffman binary tree order and other values will toggle it to perform basic alphabetical sorting

## Input and Output format:

For this huffman function to function properly, user must supply at least two legitimate file paths as argument,and by default, without specifying optional [-e][-d][-tm][-a] arguments.
The 1st file is a txt file containing the key and frequency data and the 2nd file is the output file path.

The frequency table txt file should be in a line by line format, with each line corresponding to a set of a single key and frequency number. e.g. "A - 3" .
The key should be a single character, disregard of uppercase or lowercase, and the frequency should be numeric, separated by "-"
It supports multiple keys, 1 in each line in the input file

Any space/ tabs/ character inside the input string of each line will be trimmed. 
There is no limitation on the scope of keys, except for space, tab/next line characters.

For encryption/decryption, input should be in plain text.
For decryption, the input file should contain only 1 or 0

The module will then print out the created huffman binary tree in preorder and the code table to the output file, then the encrypted content and the decrypted content, if any.

> frequency keys example: line1:a-1 , line2: b-2
>
> encode file line example: A happy life, joy to the world
> 
> decode file line example: 1101101000010001111100011111101000000101100


### Example input and output

>An example of huffman tree printout 
> 
>From Input file : `line1:a-1 , line2: b-2`
> 
>In Output file: 
>`The Tree order is AB: 3, A: 1, B: 2`
>`The code is A: 0, B: 1`

>An example of encoding
> 
>From Input file : `Hello World`
> 
>In Output file: `11011 010 0001 0001 11110 0011 11110 1000 0001 01100` (actual output will have no space)

>An example of decoding 
> 
>From Input file : `111111101111111101001010010110100011100101101010`
> 
>In Output file: `AHAPPYLIFE`
