"""create a function that takes an array and sum (integer). If there are two pairs of nums in the
array that are equal to the sum return true"""

def has_pair_with_sum(arr, s):
    #make a set
    seen_set = set()

    #loop through arr
    
    for i in range(len(arr)-1):
        #if arr[i] is in seen_set return true
        if arr[i] in seen_set:
            return True
        else:
            #subtract arr[i] from s 
            #if arr[i] in seen_set it means that it's pair that equals s has already been if s = 5 
            #and arr[i] = 3 and it's in seen set that means 2 is in the array at a previous index
            # 3 +2 = 5 return true
            seen_set.add(s - arr[i])
    return False


print(has_pair_with_sum([6,4,3,2,1,7], 9))
print(has_pair_with_sum([4,1,7], 9))

