 def move_zeroes(nums):

     #slower

        i = 0
        j = 0
        
        while j < len(nums):
            
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
            j += 1
            
def move_zeroes2(nums):
    #faster
        i = 0
        for j in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i +=1