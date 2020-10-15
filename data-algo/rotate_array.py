    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #slower

        for i in range(k):
            front = [nums.pop(-1)]
            nums[0:0] = front
            
        
        #faster
        
#         first = nums[:len(nums) - k]
#         last = nums[len(nums)-k:]
        
#         nums[:] = last + first