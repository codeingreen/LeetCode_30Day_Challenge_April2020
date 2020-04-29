class FirstUnique:

    def __init__(self, nums: List[int]):
        
        self.dict = collections.OrderedDict()
        self.nums = nums
        
        for num in nums:
            self.dict[num] = self.dict.get(num, 0) + 1
            

    def showFirstUnique(self) -> int:
        
        for key, value in self.dict.items():
            if value ==1:
                return key
            
        return -1
        
    def add(self, value: int) -> None:
        
        self.nums.append(value)
        self.dict[value] = self.dict.get(value, 0) + 1
        
