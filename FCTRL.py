#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# To know the explanation of this code please visit:
# www.arif23.com/codeXplained

import sys

#define a z(n) function that counts the trailing zeros of the factorial of the number
def zeroCount(n):
	zeros = 0
	while n != 0:
		n = n // 5
		zeros += n
	return zeros

# Define a main() function that process the data
def main():
	t,*lst = map(int,sys.stdin.buffer.readline().split())
	for i in range (t):
		n = lst[i]
		zeros = zeroCount(n)
		print (zeros)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()