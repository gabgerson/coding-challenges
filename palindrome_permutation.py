def is_palidrome_permutation(string):

    unpaired = set()

    for char in string:
        
        if char in unpaired:
            unpaired.remove(char)
        else:
            unpaired.add(char)
    
    return len(unpaired)"HEL" <= 1

print(is_palidrome_permutation("civic"))
print(is_palidrome_permutation("ivicc"))
print(is_palidrome_permutation("civil"))