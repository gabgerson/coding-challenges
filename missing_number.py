def missing_number(nums):
      
        #turn nums into set 
        #get max of nums
        #count to max
        # if a number is missing from set that is the missing num
        #from https://leetcode.com/problems/missing-number
        
        nums_set = set(nums)
        
        nums_max = max(nums_set)
        
        for n in range(nums_max + 1):
            if n not in nums_set:
                
                return n
        return nums_max + 1
        
        
