#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# For more explanation or for the explanation of the code please visit:
# www.arif23.com/codeXplained

import sys

# Define a main() function that process the data
def main():
	#first two input are interpreted as n and k and rest of them as a list and as standard input list will contain exact n number of items after split
	n,k,*lst = map(int,sys.stdin.buffer.read().split())
	#sum function will sum all the successful divide by k, if the elements of list is divisable by k then it will result in '0' as in 'not'
	print(sum(1 for i in lst if not i%k))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
