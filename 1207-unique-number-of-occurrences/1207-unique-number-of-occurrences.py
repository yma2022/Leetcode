class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        oc = dict()
        for num in arr:
            if num in oc:
                oc[num] += 1
            else:
                oc[num] = 1
        return len(oc) == len(set(oc.values()))
            