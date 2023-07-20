class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        origin = image[sr][sc]
        if origin == color:
            return image
        def dfs(x,y):
            for dx,dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0<=nx<len(image) and 0<=ny<len(image[0]) and image[nx][ny] == origin:
                    image[nx][ny] = color
                    dfs(nx, ny)
            return
        dfs(sr,sc)
        image[sr][sc] = color
        return image
        