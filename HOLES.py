#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# Form more information and explanation please visit:
# www.arif23.com/codexplained

import sys

# Define a main() function that process the data
def main():
	h = ['A','D','O','P','R','Q']
	t = int(input())
	for i in range (t):
		holes = 0
		s = list(input())
		for j in s:
			if(j in h):
				holes += 1
			if(j == 'B'):
				holes += 2
		print (holes)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
