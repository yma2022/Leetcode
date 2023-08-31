class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Binary search
        # for i in range(len(numbers)):
        #     left, right = i + 1, len(numbers) - 1
        #     while left < right:
        #         mid = (left + right) // 2
        #         if numbers[mid] < target - numbers[i]:
        #             left = mid + 1
        #         else:
        #             right = mid
        #     if numbers[i] + numbers[left] == target:
        #         return [i + 1, left + 1]
        
        # Two pointers
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1