#!/usr/bin/env python3

# Imports
import sys
import os
from functools import reduce

# Inputs

sys.argv = (0, "Example_files/16bits_1998", 0)  # Testing purposes

if len(sys.argv) < 3:
	raise ValueError("Missing input_file (file path as string) or mode (0 or 1) arguments.")
else:
	input_file = sys.argv[1]
	mode = sys.argv[2]  # 0 to decode, 1 to encode
	if not os.path.exists(input_file):
		raise FileNotFoundError("input_file was not found.")
	if mode not in (0, 1):
		ValueError("Supported modes are: 0 for decoding, and 1 for encoding.")

if len(sys.argv) == 3:
	if mode == 0:
		output_file = "Decoded" + input_file
	elif mode == 1:
		output_file = "Encoded" + input_file
else:
	output_file = sys.argv[3]


# Functions


def hamming_decode(bits):
	dec_pos = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
	return dec_pos


def hamming_encode(bits):
	print("Not functioning ATM")
	print(bits)
	pass


def main():
	with open(input_file, 'r') as inp:
		input_bits = inp.read()
	if mode == 0:
		output_bits = hamming_decode(input_bits)
	elif mode == 1:
		output_bits = hamming_encode(input_bits)
	with open(output_file, 'w+') as outp:
		if output_bits:
			outp.write(str(output_bits))

# Main execution


if __name__ == "__main__":
	main()
