# Binary search note

## What is binary search?

Binary search is a fundamental algorithm used mainly in ordered data structures.

```
Terminology used in Binary Search:

- Target - the value that you are searching for
- Index - the current location that you are searching
- Left, Right - the indicies from which we use to maintain our search Space
- Mid - the index that we use to apply a condition to determine if we should search left or right
```

## What is the trick?

To start binary search, there are few important steps:
- Make the data structure in order.
- Determine lower and upper bound to start searching.
- Decide the region to search.

### Template

#### [left, right)

When search single element in e.g. array, it is easy to use the following template. 

```
def binarySearch(arr, target):
    left, right = low, high
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return
```

There are few examples for this template:
- LC 162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

```
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```

- LC 153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```

- LC 154. Find Minimum in Rotated Sorted Array II

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                right -= 1
        return nums[left]
```

- LC 719. Find K-th Smallest Pair Distance

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

```
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def get_count(dist):
            left, count = 0, 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > dist:
                    left += 1
                count += (right - left)
            return count

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if get_count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
```

- LC 410. Split Array Largest Sum

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

```
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def get_count(x):
            total = 0
            count = 1
            for num in nums:
                if total + num > x:
                    count += 1
                    total = num
                else:
                    total += num
            return count

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if get_count(mid) > k:
                left = mid + 1
            else:
                right = mid
        return left
```


#### [left, right]

In some cases, it would be easy to use closed region to complete the search. For example, it is more concise to use this template if searching a region of repetive numbers (LC 34). 

```
def binarySearch(arr, target):
    left, right = low, high
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return
```

There are few examples for this template:
- LC 33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
```

- LC 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

```
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, val):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < val:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return left if nums[left] == val else -1
        
        def findRight(nums, val):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= val:
                    left = mid + 1
                else:
                    right = mid - 1 
            return right if nums[right] == val else -1
        
        if not nums or target > nums[-1] or target < nums[0]:
            return [-1, -1]
        left = findLeft(nums, target)
        right = findRight(nums, target)
        
        return [left, right]
```

In this case if we use template 1 to search the left bound, the function would be mostly the same by only changing the while loop condition and ```right``` calculation. When searching for the right bound, however the function would be less intuitive (code below). 

```
        def findRight(nums, val):
            left, right = 0, len(nums) - 1
            if nums[right] == val:
                return right
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= val:
                    left = mid + 1
                else:
                    right = mid
            if nums[right - 1] == val:
                return right - 1
            else:
                return -1
```

