#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# Form more information and explanation please visit:
# www.arif23.com/codexplained

import sys
import os

# Define a openFile() function that opens a file and read it and output to another file
def openFile():
	# Open input and output files
	file1 = "io-sample/input.txt"
	file2 = "io-sample/output.txt"
	inputFile = open(file1,"r")
	outputFile = open(file2,"w")

	# Write to output file
	# In python 3.x versions write() doesn't support string - it can be done with encoding
	status = os.stat(file1)
	print (status.st_mtime)
	lines = inputFile.read()
	print (lines)
	output = outputFile.write(lines)

	# Close open files
	inputFile.close()
	outputFile.close()

# Define a main() function that process the data
def main():
	openFile()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()