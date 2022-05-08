#File Name Input: F:\PROGRAMMING\Python Repo\LR1\LR1\text.txt

fileName = input("Enter the file name: ")
file = open(fileName, 'r')
lineCount = 0

for line in file:
    lineCount += 1

print("Number of lines in the file = ", lineCount)

print("==========================================")
print("Input a LINE NUMBER to display the text ")
print("Input '0' to END the program ")
print("==========================================")

while True:
    linenum = 0
    num = int(input("Input: "))
    if num >= 1 and num <= lineCount:
        file = open(fileName, 'r')
        for lines in file:
            linenum += 1
            if linenum == num:
                print("Line " + str(num) + ": " + lines + "\n")
                
    else:
        if num == 0:
            print("The program ends here")
            break
