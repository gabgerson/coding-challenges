""" merge sorted arrays 
 ex:
 [0,3,4,31] and [4,6,30] become 

 [0,3,4,6,30,31]
"""
#easy way
def merge_easy_way(arr1,arr2):
    arr1.extend(arr2)
    arr1.sort()
    return arr1

def merge_sorted_arrays(arr1,arr2):

    #loop and compare index of arr1 top index or arr2 and add lesser to new array
    # new array

    merged_arr = []


    i = 0
    j = 0
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    
    while i < len(arr1) or j < len(arr2):
        if i == len(arr1):
            merged_arr.extend(arr2[j:])
            return merged_arr
        elif j == len(arr2):
            merged_arr.extend(arr1[i:])
            return merged_arr
        else:
            if arr1[i] < arr2[j]:
                merged_arr.append(arr1[i])
                i += 1
            else:
            
                merged_arr.append(arr2[j])
                j +=1
              
print(merge_easy_way([0,3,4,31],[4,6,30]))
print(merge_sorted_arrays([0,3,4,31],[4,6,30]))