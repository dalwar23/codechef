#!/usr/bin/python -tt
# Copyright Md Dalwar Hossain Arif
# Form more information and explanation please visit:
# www.arif23.com/codexplained

import sys

# Define a main() function that process the data-
def main():
    t, *lst = map(int,sys.stdin.buffer.read().split())
    s = sorted(lst)
    for i in range(t):
        print (s[i])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
main() 
