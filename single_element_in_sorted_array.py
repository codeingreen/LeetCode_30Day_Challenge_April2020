# O(N) solution


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        i = nums.pop(0)
        
        for num in nums:
            i ^=num
        
        return i
        
