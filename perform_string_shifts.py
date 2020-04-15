class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        if not s or len(s) == 0:
            return ''
        
        if len(shift) == 0:
            return ''
        
        s = list(s)
        
        for index in shift:
            
            [direction, amount] = index
            
            while amount !=0:
                if direction == 0:
                    temp = s.pop(0)
                    s.append(temp)
                    amount -=1
                elif direction ==1:
                    temp = s.pop()
                    s.insert(0, temp)
                    amount -=1
        
        print(s)
        
        s = ''.join(s)
        
        return s
                    
