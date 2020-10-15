    def containsDuplicate(nums):

        # make set
        seen = set()
        
        #loop through nums
        
        for num in nums:
            #if num has been seen return true
            if num in seen:
                return True
            else:
            # add num to set
                seen.add(num)
        #if no item has been seen twice return false
        return False