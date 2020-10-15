def max_sub_array(nums):

        
    max_sum = current_sum = nums[0] 
    
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
        else:
            current_sum += nums[i]
        max_sum = max(max_sum,current_sum)
    
    return max_sum

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))