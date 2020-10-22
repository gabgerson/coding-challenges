"""Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""


def find_high_product_of_3(arr):
    if len(arr) < 3:
        return "less than 3"
    highest = max(arr[0],arr[1])
    lowest = min(arr[0], arr[1])
    highest_product_3 = arr[0] * arr[1] * arr[2]
    highest_product_2 = 0
    lowest_pro_2 = 0
    

    #loop though list
    for i in range(2, len(arr)):
        curr = arr[i]

        highest_product_3 = max(highest_product_3, curr * lowest_pro_2, curr * highest_product_2)

        highest_product_2 = max(highest_product_2, curr * lowest, curr * highest)

        lowest_pro_2 = min(lowest_pro_2, curr * highest, curr * lowest)

        highest = max(highest, curr)
        lowest = min(lowest, curr)
    return highest_product_3

print(find_high_product_of_3([1,5,7,4,3,9]))
print(find_high_product_of_3([1, 10, -5, 1, -100]))
