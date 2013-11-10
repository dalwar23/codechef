#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# Form more information and explanation please visit:
# www.arif23.com/codexplained

import sys

# Define a openFile() function that opens a file and read it and output to another file
def openFile():
	# Open input and output files
	inputFile = open("io-sample/input.txt","r")
	outputFile = open("io-sample/output.txt","wb")

	# Write to output file
	# In python 3.x versions write() doesn't support string - it can be done with encoding
	for line in inputFile:
		line = inputFile.readline()
		outputFile.write(bytes(line,"utf-8"))

	# Close open files
	inputFile.close()
	outputFile.close()

# Define a main() function that process the data
def main():
	openFile()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()