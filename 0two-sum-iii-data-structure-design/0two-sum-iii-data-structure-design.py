class TwoSum:

    def __init__(self):
        self.nums = []
        

    def add(self, number: int) -> None:
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        d = set()
        for n in self.nums:
            if n in d:
                return True
            d.add(value - n)
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)