import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 0:
            return True
        
        if num == 1:
            return True
        
        print(num, math.sqrt(num))
        
        value = math.sqrt(num)
        if int(value) * int(value) == num:
            return True
        
        return False
