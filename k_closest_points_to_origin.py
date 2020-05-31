import math

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        if len(points) == 0:
            return [[]]
        
        if K == 0:
            return [[]]
        
        dist = []
        distance_list = []
        
        for point in points:
            distance = sqrt((0-point[0])**2 + (0-point[1])**2)
            distance_list.append([distance, point])
        
        distance_list.sort()
        values = distance_list[:K]
        
        result = []
        
        for val in values:
            result.append(val[1])
            
        
        return result
            
        
 
            
      
        
