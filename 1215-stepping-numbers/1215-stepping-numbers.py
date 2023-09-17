class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        res = []
        
        q = deque()
        for i in range(1, 10):
            q.append(i)

        if low == 0:
            res.append(0)
            
        while q:
            # print(q)
            p = q.popleft()
            if p < high:
                last = p % 10
                if last > 0:
                    if p * 10 + last - 1 <= high:
                        q.append(p * 10 + last - 1)
                if last < 9:
                    if p * 10 + last + 1 <= high:
                        q.append(p * 10 + last + 1)
            if p >= low and p <= high:
                res.append(p)
        return res