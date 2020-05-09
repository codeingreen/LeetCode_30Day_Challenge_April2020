class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        coordinates.sort(key =lambda x: x[0])
        
        print(coordinates)
        
        i = 0
        j = 1
        k = 2
        

        if (len(set([x[0] for x in coordinates])) == 1) or (len(set([x[1] for x in coordinates])) == 1):
            return True
        
        while i <j and j <k and k < len(coordinates):
            
            diff_y2_y1 = coordinates[j][1] - coordinates[i][1]
            diff_x2_x1 = coordinates[j][0] - coordinates[i][0]
            
            diff_y3_y1 = coordinates[k][1] - coordinates[i][1]
            diff_x3_x1 = coordinates[k][0] - coordinates[i][0]
            
            # taking divide by zero into consideration, otherwise the slope has to be equal
            if diff_x2_x1 != 0 and diff_x3_x1!=0:
            
                print(diff_y2_y1, diff_x2_x1, diff_y3_y1, diff_x3_x1)

                if (diff_y2_y1 / diff_x2_x1) != (diff_y3_y1 / diff_x3_x1):
                    return False

            i +=1
            j +=1
            k +=1

        
        return True
    
            
        
