class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        m = collections.Counter(nums)
        
        for key in m:
            print(key, m[key])
            if m[key] > len(nums)//2:
                return key
        
