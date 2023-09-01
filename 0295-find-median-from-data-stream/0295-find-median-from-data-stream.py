class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, num)
        heapq.heappush(self.high, -self.low[0])
        heapq.heappop(self.low)
        
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -self.high[0])
            heapq.heappop(self.high)
        
        

    def findMedian(self) -> float:
        return float(self.low[0]) if len(self.low) > len(self.high) else (self.low[0] - self.high[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()