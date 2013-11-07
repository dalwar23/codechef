#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# To know the explanation of this code please visit:
# www.arif23.com/codexplained

import sys

#define a z(n) function that counts the trailing zeros of the factorial of the number
def zCount(n):
	z = 0
	while n >= 5:
		n //=  5
		z += n
	return z

# Define a main() function that process the data
def main():
	t,*lst = map(int,sys.stdin.buffer.read().split())
	for i in range (t):
		n = lst[i]
		z = zCount(n)
		print (z)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
