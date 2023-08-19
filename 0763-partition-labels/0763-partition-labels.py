class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = [i, i]
            else:
                hashmap[s[i]][1] = i
        common = [0, 0] 
        ans = []
        for key in hashmap:
            if hashmap[key][0] <= common[1]:
                common = [min(hashmap[key][0], common[0]), max(hashmap[key][1], common[1])]
            else:
                ans.append(common[1] - common[0] + 1)
                common = hashmap[key]
        ans.append(common[1] - common[0] + 1)
        return ans
        