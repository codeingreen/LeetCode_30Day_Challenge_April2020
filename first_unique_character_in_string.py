class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if len(s) == 0:
            return -1
        
        idx = collections.OrderedDict()
        
        for i in range(len(s)):
            if s[i] in idx:
                idx[s[i]] = idx[s[i]] + 1
            else:
                idx[s[i]] = 1
            
        for key, value in idx.items():
            if value == 1:
                return s.index(key)
            
        return -1
                    
                
        
            
        
        
