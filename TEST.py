#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# www.arif23.com/codeXplained

import sys

# Define a main() function that process the data
def main():
	while True:
		i = int(input())
		if i==42:
			break
		else:
			print(i)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()