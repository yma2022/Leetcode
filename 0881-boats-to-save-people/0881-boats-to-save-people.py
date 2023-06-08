class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left, right = 0, n - 1
        cnt = 0
        
        while left <= right:
            total = people[left] + people[right]
            if total > limit:
                cnt += 1
                right -= 1
            else:
                cnt += 1
                left += 1
                right -= 1
        
        # print(left, right)
        return cnt
            