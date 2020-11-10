def merge(arr1, arr2):
    left_i, right_i = 0, 0
    merged_ls = []
    count = 0
    l1 = len(arr1)
    l2 = len(arr2)
    _append = merged_ls.append
    while left_i < l1 and right_i < l2:
        if arr1[left_i] <= arr2[right_i]:
            _append(arr1[left_i])
            left_i += 1
        else:
            _append(arr2[right_i])
            right_i += 1
            count += l1 - left_i
            #count is how many times left elements gets skipped
    merged_ls += arr1[left_i:]
    merged_ls += arr2[right_i:]
    return  merged_ls, count

def merge_sort(arr):
    len_arr = len(arr)
    mid = len_arr // 2
    
    if len_arr > 1:
        left, left_count = merge_sort(arr[:mid])
        right, right_count = merge_sort(arr[mid:])
        merged, count = merge(left,right)

   
        return merged, count + left_count + right_count
        
    return arr, 0

def countInversions(arr):
    
    ls, count = merge_sort(arr)
    return count
    

print(countInversions([2,1,4,5,7,3]))