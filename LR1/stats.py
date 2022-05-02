#MODE, MEDIAN, MODE FUNCTIONS
def mode(numbers):

    count = []
    for i in numbers:
        count.append(numbers.count(i))
    uniq_cnt = []
    for i in count:
        if i not in uniq_cnt:
            uniq_cnt.append(i)
    if len(uniq_cnt) > 1:
        m = []
        for i in list(range(len(count))):
            if count[i] == max(uniq_cnt):
                m.append(numbers[i])
        mode = []
        for i in m:
            if i not in mode:
                mode.append(i)
        return mode
    else:
        print("There is NO mode in the data set")

def median(numbers):

    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        med = (numbers[midpoint])
    else:
        med = ((numbers[midpoint] + numbers[midpoint - 1]) / 2)

    return med

def mean(numbers):

    mean = 0
    for i in numbers:
        mean += i
    mean /= len(numbers)

    return mean

#MAIN
num = [34, 56, 23, 87, 34, 78, 26, 41, 71, 90, 51, 51, 34, 98]

print("List: " + str(num) + "\n")

print("Mode: " + str(mode(num)))
print("Median: " + str(median(num)))
print("Mean: " + str(mean(num)))



