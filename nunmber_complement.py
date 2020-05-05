class Solution:
    def findComplement(self, num: int) -> int:
        
        if num == 0:
            return 0
        
        binary_of_num = "{0:b}".format(num)
        
        # number of bits in that number
        bits = int(math.log2(num)) + 1
        
        # flip bits in that number
        for i in range(bits):
            num = (num ^ (1 << i))  
        
        print(num)
        
        return num
        
