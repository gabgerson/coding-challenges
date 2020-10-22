def get_products_of_all_ints_except_at_index(arr):

    if len(arr) < 2:
        return arr

    products_excluding_current = [None] * len(arr)
    product_so_far = 1


    


    for i in range(len(arr)):
        products_excluding_current[i] = product_so_far 

        product_so_far = product_so_far * arr[i]

    # traverse list backwards


    product_so_far = 1

    for i in range(len(arr)-1, -1, -1):
        print(i)
        products_excluding_current[i] *= product_so_far 
        product_so_far = product_so_far * arr[i]

    return products_excluding_current



print(get_products_of_all_ints_except_at_index([1, 0, 3, 4]))


