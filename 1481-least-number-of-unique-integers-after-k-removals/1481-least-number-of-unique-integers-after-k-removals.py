class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = collections.Counter(arr)
        srt = sorted(arr,key = lambda x:(d[x],x))
        return len(set(srt[k:]))