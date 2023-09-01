# Heap and priority queue note

## What is heap and priority queue?

A priority queue is an abstract data type similar to a regular queue or stack data structure in which each element additionally has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority.

A common misconception is that a Heap is the same as a Priority Queue, which is not true. A priority queue is an abstract data type, while a Heap is a data structure. Therefore, a Heap is not a Priority Queue, but a way to implement a Priority Queue.

According to Wikipedia, a Heap is a special type of binary tree. A heap is a binary tree that meets the following criteria:
- Is a complete binary tree;
- The value of each node must be no greater than (or no less than) the value of its child nodes.


A Heap has the following properties:
- Insertion of an element into the Heap has a time complexity of O(logN);
- Deletion of an element from the Heap has a time complexity of O(logN);
- The maximum/minimum value in the Heap can be obtained with O(1) time complexity.

Classification of Heap
- There are two kinds of heaps: Max Heap and Min Heap.
- Max Heap: Each node in the Heap has a value no less than its child nodes. Therefore, the top element (root node) has the largest value in the Heap.
- Min Heap: Each node in the Heap has a value no larger than its child nodes. Therefore, the top element (root node) has the smallest value in 

## What is the trick to implement pq with heap?
- Construct min heap is straighforward by heapifying array
- Trick in constructing max heap is to multiply each element in the array by -1, then heapify with modified elements.
- Common heap functions in python:

  * heapify() function takes an array as input and converts it into a heap. The heap property is then maintained by the heapq module.
  * heappush() function takes an element as input and adds it to the heap. The heap property is then maintained by the heapq module.
  * heappop() function removes the smallest element from the heap. The heap property is then maintained by the heapq module.

## Template

The implementation here is the general use of heap, think about the features of min/max heap before using.

```
Class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    def heapAdd(self, num):
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, - num)
    def heapTop(self):
        minTop = heapq.heappop(self.minHeap)
        maxTop = - heapq.heappop(self.maxHeap)
```

### LC 295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

#### Solution:
The thought here is to implement two heaps, one min heap and one max heap. The sizes of the two heaps are balanced (minHeap.size == maxHeap.size or minHeap.size == maxHeap.size + 1). The minHeap keeps large numbers while the maxHeap keeps small numbers. This way, the median can be found by the top value of the two heaps.
```
class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -self.low[0])
        heapq.heappop(self.low)
        
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -self.high[0])
            heapq.heappop(self.high)
        
        

    def findMedian(self) -> float:
        return float(- self.low[0]) if len(self.low) > len(self.high) else (- self.low[0] + self.high[0]) / 2
```

### LC 1167. Minimum Cost to Connect Sticks

You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

#### Solution:
The minimm cost is to use the two shortest sticks every time till there is only one stick. Thus this can be solved with min heap.

```
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        pq = sticks
        heapq.heapify(pq)
        
        cost = 0
        
        while len(pq) > 1:
            stick1 = heapq.heappop(pq)
            stick2 = heapq.heappop(pq)
            
            new_stick = stick1 + stick2
            cost += new_stick
            heapq.heappush(pq, new_stick)
        
        return cost
```

## LC 1642. Furthest Building You Can Reach

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

#### Solution:
The idea here is to leave large eight differences to ladders, this indicate the use of min heap.
```
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            
            if climb <= 0:
                continue
            heapq.heappush(ladder_allocations, climb)
            
            if len(ladder_allocations) <= ladders:
                continue
            bricks -= heapq.heappop(ladder_allocations)
            
            if bricks < 0:
                return i
            
        return len(heights) - 1
```


