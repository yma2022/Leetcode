# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.val = []        

    def getRandom(self) -> int:
        if self.val:
            return self.val[random.randint(0,len(self.val)-1)]
        curr = self.head
        while curr:
            self.val.append(curr.val)
            curr= curr.next
        return self.val[random.randint(0,len(self.val)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()