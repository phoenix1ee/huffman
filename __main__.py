#Shun Fai Lee Lab3
from pathlib import Path
import argparse
from time import time_ns
from huffman.builder import build
from huffman.encoder import encoder
from huffman.decoder import decoder

# use the Argument parser to define compulsory and optional arguments
this_parser = argparse.ArgumentParser(description ='use huffman compression to encode/decode message')
this_parser.add_argument("fq_file", type=str, help="Frequency Table File Pathname")
this_parser.add_argument("-e", type=str, required=False, help="Optional, Pending encryption File Pathname")
this_parser.add_argument("-d", type=str, required=False, help="Optional, Pending decryption File Pathname")
this_parser.add_argument("out_file", type=str, help="Output File Pathname")
this_parser.add_argument('-tm', type=bool, choices=[True, False], default=False, required=False, action='store', help="Optional processing timer (default: False)")
this_parser.add_argument('-a', type=bool, choices=[True, False], default=False, required=False, action='store', help="Optional encode/decode analysis details (default: False)")
args = this_parser.parse_args()

# Set the input and output file path
fq_path = Path(args.fq_file)
if args.e:
    e_path = Path(args.e)
if args.d:
    d_path = Path(args.d)
out_path = Path(args.out_file)
if args.tm:
    start_time = time_ns()

if fq_path.is_file():
    #proceed the frequency table file if exist, build and print to file
    with (fq_path.open('r') as frq_file, out_path.open('w') as output_file):
        Hufftree = build(frq_file,output_file)
        if not Hufftree:
            raise Exception("Please verify input frequency table")
else:
    raise Exception(f'frequency table file in {fq_path.absolute()} do not exist')
if args.e:
    if e_path.is_file():
    #proceed the encode of input file if exist
        with (e_path.open('r') as en_file, out_path.open('a') as output_file):
            output_file.write(f'encoding result from {e_path}:' + "\n")
            encoder(en_file, output_file, Hufftree, args.a)
    else:
        raise Exception(f'file to encrypt in {e_path.absolute()} do not exist')
if args.d:
    if d_path.is_file():
    #proceed the decode of input file if exist
        with (d_path.open('r') as d_file, out_path.open('a') as output_file):
            output_file.write(f'decoding result from {d_path}:'+"\n")
            decoder(d_file,output_file,Hufftree, args.a)
    else:
        raise Exception(f'file to encrypt in {e_path.absolute()} do not exist')

if args.tm:
    with (out_path.open('a') as output_file):
        end_time = time_ns()
        output_file.write("---------------------------------------------" + "\n")
        output_file.write(f'Start time: {"%.2f" % start_time} ns' + "\n")
        output_file.write(f'process time: {"%.2f" % (end_time - start_time)} ns')