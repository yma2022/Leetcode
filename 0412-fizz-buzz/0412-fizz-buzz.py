class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0 for _ in range(n)]
        for i in range(n):
            r3 = (i+1) % 3
            r5 = (i+1) % 5
            if r3+r5 == 0:
                res[i] = 'FizzBuzz'
            elif r3 == r3+r5:
                res[i] = 'Buzz'
            elif r5 == r3+r5:
                res[i] = 'Fizz'
            else:
                res[i] = str(i+1)
        return res