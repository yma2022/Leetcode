class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        
        def dfs(x):
            seen[x] = True
            for nei in rooms[x]:
                if not seen[nei]:
                    dfs(nei)
        
        dfs(0)
        print(seen)
        return all(seen)
            
            
        