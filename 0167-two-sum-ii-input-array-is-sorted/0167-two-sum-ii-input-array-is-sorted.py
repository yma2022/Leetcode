class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                mid = (left + right) // 2
                if numbers[mid] < target - numbers[i]:
                    left = mid + 1
                else:
                    right = mid
            if numbers[i] + numbers[left] == target:
                return [i + 1, left + 1]