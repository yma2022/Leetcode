class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
        arr1_min, arr1_max = min(arr1), max(arr1)
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = arr1_max - arr1_min + 1
        counts = [0 for _ in range(size)]

        # 统计值为 num 的元素出现的次数
        for num in arr1:
            counts[num - arr1_min] += 1

        res = []
        for num in arr2:
            while counts[num - arr1_min] > 0:
                res.append(num)
                counts[num - arr1_min] -= 1

        for i in range(size):
            while counts[i] > 0:
                num = i + arr1_min
                res.append(num)
                counts[i] -= 1
        
        return res