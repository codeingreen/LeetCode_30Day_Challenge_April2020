class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # remove the largest k values from the MSB
        
        smallest = ''
        new_length = len(num) - k
        
        # special case
        if len(num) == k:
            return '0'
        
        if len(num) < k:
            return num
        
        number = []
        for n in num:
            number.append(int(n))
        
        l = 0
        r = l+1
        
        while len(number) != new_length and (l < r) and (r < len(number)):
            
            if number[l] > number[r]:
                number.pop(l)
                l = 0
                r = l+1
            # if they are equal or less
            else:
                l+=1
                r = l+1
        
        while len(number) != new_length:
            max_number_index = number.index(max(number))
            number.pop(max_number_index)
            
        if len(number) == 1:
            return str(number[0])
        
        # remove all leading zeros
        while len(number) > 0:
            if number[0] == 0:
                number.pop(0)
            else:
                break
        
        if len(number) == 0:
            return '0'    
        
        return ''.join([str(x) for x in number])
                
            
                
        
        
        
