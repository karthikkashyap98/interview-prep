#!/bin/python3

import math
import os
import random
import re
import sys


'''
Input Format

The first line contains an integer, n , the size of the array a. 
The second line contains n space-separated integers a[i].


Output Format

You must print the following three lines of output:

Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
First Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.


'''
# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    countSwaps = 0
    for i in range(n):
        swapped = False

        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                countSwaps = countSwaps + 1
                swapped = True
            
        if swapped == False:
            break       
    firstelement = a[0] 
    lastelement = a[n-1]    

    print("Array is sorted in {countSwaps} swaps.".format(countSwaps = countSwaps))

    print("First Element:",firstelement)

    print("Last Element:",lastelement )

    



if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
