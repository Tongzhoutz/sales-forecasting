# data数组中查找16: reply its index; otherwise return -1
data1 = [24, 18, 12, 9, 16, 66, 32, 4]
data2 = [18, 24, 12, 9, 3, 66, 32, 4]


def find_index(data, target):
    n = len(data)
    for i in range(n):
        if data[i] == target:
            return i
    # after going through all elements; if no match, return -1
    return -1
print("The index we hope to seek is %d" % find_index(data1, 9))
print(find_index(data2, 24))

