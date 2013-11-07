#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# Form more information and explanation please visit:
# www.arif23.com/codexplained

import sys

# Define a main() function that process the data-
def main():
	lst = []
	t = int(input())
	for i in range(t):
		item = int(input())
		lst.append(item)
	s = sorted(lst)
	for j in range (len(s)):
		print (s[j])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
