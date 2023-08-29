class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [0] * (len(customers) + 1)
        d = Counter(customers)
        prefix[-1] = d["N"]
        for i in range(len(customers) - 1, -1, -1):
            if customers[i] == "Y":
                prefix[i] = prefix[i + 1] + 1
            else:
                prefix[i] = prefix[i + 1] - 1
        return prefix.index(min(prefix))
        