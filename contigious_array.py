class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) == 0 or len(nums) ==1:
            return 0
        
        summation = 0
        sum_dict = dict()
        sum_dict[0] = -1
        
        res = 0
        
        for i in range(0, len(nums)):
            
            if nums[i] ==1:
                summation +=1
            else:
                summation -=1
            
            if summation in sum_dict:
                res = max(res, i- sum_dict[summation])
            else:
                sum_dict[summation] = i
                
        return res
