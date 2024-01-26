class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[1])
        
        st = []
        for interval in intervals:
            while st and st[-1][-1] >= interval[0]:
                temp = st.pop()
                interval = [min(temp[0], interval[0]), max(temp[1], interval[1])]
            st.append(interval)
                
        return st
        