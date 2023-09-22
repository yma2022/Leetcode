class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) < len(list2):
            list1, list2 = list2, list1
            
        d = collections.defaultdict(list)
        key = float('inf')
        for w1 in list1:
            if w1 in list2:
                index_sum = list1.index(w1) + list2.index(w1)
                d[index_sum].append(w1)
                key = min(key, index_sum)
                
        return d[key]
        