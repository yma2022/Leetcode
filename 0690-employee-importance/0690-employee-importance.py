"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = collections.defaultdict()
        for i in range(len(employees)):
            graph[employees[i].id] = i
        res = []
        res.append(employees[graph[id]].importance)
        def dfs(id):
            for xid in employees[graph[id]].subordinates:
                res.append(employees[graph[xid]].importance)
                if employees[graph[xid]].subordinates:
                    dfs(xid)
            return
        
        dfs(id)
        return sum(res)
                    

            