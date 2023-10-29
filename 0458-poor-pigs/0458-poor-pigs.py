class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        n = round(math.log(buckets) / math.log(states), 9)
        print(math.log(buckets) / math.log(states))
        return math.ceil(n)
        