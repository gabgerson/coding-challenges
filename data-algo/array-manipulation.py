def arrayManipulation(n, queries):


    arr = [0] * n
    for item in queries:
        arr[item[0] - 1] += item[2]
        if item[1] != len(arr):
            arr[item[1]] -= item[2]

    max_num = 0
    num = 0

    for i in arr:
        num += i
        if max_num < num:
            max_num = num

    return max_num