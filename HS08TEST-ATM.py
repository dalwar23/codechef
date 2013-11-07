#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# For more info and explanation of the code please visit:
# www.arif23.com/codeXplained

import sys

# Define a main() function that process the data
def main():
	t = input()
	t = t.split(" ")

	wth = float(t[0])
	bl = float(t[1])

	if wth % 5 == 0 and wth+0.5 < bl:
		n_bl = bl - (wth + 0.50)
	else:
		n_bl = bl
	print ("%.2f"%n_bl)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
