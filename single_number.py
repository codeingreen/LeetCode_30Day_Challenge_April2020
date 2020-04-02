'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
Example 2:
Input: [4,1,2,1,2]
Output: 4
'''
------

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        digits = dict()
        
        for num in nums:
            if num not in digits:
                digits[num] = 1
            else:
                digits[num] +=1
                
        for key, value in digits.items():
            print(key, '=>', value)
            if value == 1:
                return key
