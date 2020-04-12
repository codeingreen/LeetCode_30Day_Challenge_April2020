'''
class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        # sort array to count better
        arr.sort()
        
        if not arr or len(arr) == 0:
            return 0
        
        if len(arr) == 1:
            return 0
        
        count = 0
        
        counted = [False] * len(arr)
        
        for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] +1 == arr[j]:
                    if not counted[i]:
                        counted[i] = True
                        count +=1
        
        return count
        
'''
