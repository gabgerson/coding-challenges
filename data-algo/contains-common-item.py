"""given 2 arrays, create a function that let's a user know (true/false) 
whether these two arrays contain any common items
for example:
    ex1:
    arr1 = ['a', 'b','c','x']
    arr2 = ['z', 'y', 'i']
    should return false
    
    ex2:
    arr1 = ['a', 'b','c','x']
    arr2 = ['z', 'y', 'x']

    should return true

"""

def find_common_item(arr1, arr2):
    #make arr1 a set  
    arr1_set = set(arr1) #O(n) runtime

    #loop through arr2 and check if item is in arr1 set

    for item in arr2: #O(n)
        if item in arr1_set:
            return True
    
    return False
#O(m+n)

print(find_common_item(['a', 'b','c','x'],['z', 'y', 'x']))
print(find_common_item(['a', 'b','c','x'],['z', 'y', 'i']))
print(find_common_item([],[]))