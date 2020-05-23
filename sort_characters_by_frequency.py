class Solution:
    def frequencySort(self, s: str) -> str:
        
        s = sorted(s)
        
        cdict = {}
        
        for c in s:
            cdict[c] = cdict.get(c, 0) + 1
        
        v_sorted = sorted(cdict.values(), reverse=True)
        output = ''
        
        for v in v_sorted:
            for k1, v1 in cdict.items():
                if v1 == v:
                    for i in range(v):
                        output +=str(k1)
                    break
            del cdict[k1]
        
        return output
            
        
