class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N == 0:
            return 0
        
        if N ==1:
            return 1
        
        if len(trust) == 0:
            return 0
        
        if len(trust) == 1:
            for t in trust:
                if t[0] !=t[1]:
                    return t[1]
        
        # first index and second index
        se = []
        fe = []
        
        for t in trust:
            fe.append(t[0])
            se.append(t[1])
        
        for num in se:
            if num in fe:
                continue
            else:
                print(num)
                for i in range(1, N+1):
                    if i!= num:
                        if [i, num] not in trust:
                            num = -1
                            break
                        else:
                            continue
                            
                return num
        
        return -1
        
            
            
        
