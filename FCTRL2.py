#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# For more information please visit:
# www.arif23.com/codexplained

import sys

# Define a getFactorial(n) function that gives out put of factorial of any given number < 100
def getFactorial(n):
	while n <= 100:
		for j in range(1,n):
			n = n * j
		return n

# Define a main() function that process the data
def main():
	t, *lst = map(int,sys.stdin.buffer.read().split())
	for i in range (t):
		n = lst[i]
		factorial = getFactorial(n)
		print (factorial)

# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
  main()
