Day 3: Intro to Conditional Statements

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if( N%2!= 0): 
        print("Weird")
    elif (N%2 == 0):
        if N > 20:
         print("Not Weird")
        elif (2<N<5):
         print("Not Weird")
        elif(6<N<=21):
         print("Weird")
