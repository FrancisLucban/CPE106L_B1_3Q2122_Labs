'''
Program: LR2_2.py
Author: Group 7 - CPE106L B1
'''

filename = input("Enter the filename: ")
f = open(filename, 'r')

words = []

words = f.readlines()

f.close()
print("Number of Lines: ", len(words))

lineInput = 1
while lineInput != 0:
    lineInput = int(input("Enter line to print(0 to exit): "))
    if lineInput < len(words) and lineInput > 0:
        print(words[lineInput - 1])
