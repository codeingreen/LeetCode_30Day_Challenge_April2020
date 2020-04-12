class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones)==0 or not stones:
            return []
        
        if len(stones) == 1:
            return stones[0]
        
        stones.sort()
        r =len(stones)-1
        l = r -1       
        
        while len(stones) > 0:
            if stones[l] == stones[r]:
                stones[l] = -1
                stones[r] = -1
                stones = [x for x in stones if x!=-1]
                if len(stones) == 0:
                    return 0
                if len(stones) == 1:
                    return stones[0]
                stones.sort()

                r =len(stones)-1
                l = r -1
                
            elif stones[l] < stones[r]:
                stones[r] = stones[r] - stones[l]
                stones[l] = -1
                stones = [x for x in stones if x!=-1]
                
                if len(stones) == 1:
                    return stones[0]
                
                stones.sort()
                
                r =len(stones)-1
                l = r -1
            else:
                r =len(stones) - 1
                l = r-1
            
            
        print(stones)
        
        if len(stones) == 1:
            return stones[0]
        
        
