def bubble_sort(ls):

    length = len(ls)
    for i in range(length):
        for j in range(length):

            if ls[i] < ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
    return ls


print(bubble_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))