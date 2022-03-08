'''
Author: Malayao, Jimwell G.
LR2_2.py
CPE106L B1 Group 7
'''

filename = input("Enter the filename: ")
f = open(filename, 'r')

words = []

for line in f:
    words.append(line)
f.close()
print("Number of Lines: ", len(words))

lineInput = 1
while lineInput != 0:
    lineInput = int(input("Enter line to print(0 to exit): "))
    if lineInput < len(words) and lineInput > 0:
        print(words[lineInput],  "\n")
