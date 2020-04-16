class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return []
        
        # calculate array length
        al = len(nums)
        
        # assign left and right array
        left = [0] * al
        right = [0] * al
        
        left[0], right[-1] = 1,1
        
        for i in range(0, al-1):
            left[i+1] = left[i] * nums[i]
        
        for j in range(al-1, 0, -1):
            right[j-1] = right[j] * nums[j]
            
        print(left, right)
        
        return [x*y for x,y in zip(left, right)]
    
        
