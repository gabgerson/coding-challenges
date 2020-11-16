def find_factorial_iterative(num):
    #store product 
    #start with one
    product = 1

    #loop through range to num - 1 don't need the - 1 because range is exclusive
    for n in (range(2, num + 1)):
    
        product = product * n
 
    #multiply current in range by product

    return product


def find_factorial_recursive(num):
    
    if num == 2:
        return num

    return find_factorial_recursive(num - 1) * num
    

print(find_factorial_iterative(5), "interative")

print(find_factorial_recursive(5), "recursive")