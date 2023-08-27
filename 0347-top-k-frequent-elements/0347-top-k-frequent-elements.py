class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #要统计元素出现频率
        d = Counter(nums)
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pq = []
        for key, freq in d.items():
            heapq.heappush(pq, (-freq, key))
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res    