class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        if len(J) == 0 or len(S) == 0:
            return 0
        
        jewels_in_j = collections.Counter(J)
        stones_in_s = collections.Counter(S)

        num_jewels = 0
        
        for item in jewels_in_j:
            if item in stones_in_s:
                num_jewels += stones_in_s[item]
        
        return num_jewels
                
