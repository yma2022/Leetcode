class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # prev = 0
        # ans = []
        # for i in range(len(arr)):
        #     while prev < arr[i] - 1:
        #         ans.append(prev + 1)
        #         prev += 1
        #     prev += 1
        # print(ans)
        # return ans[k - 1] if len(ans) >= k else arr[-1] + k - len(ans)
        
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k
        