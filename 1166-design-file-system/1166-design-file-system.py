class FileSystem:

    def __init__(self):
        self.paths = {}
        

    def createPath(self, path: str, value: int) -> bool:
        if not path or not path.split("/"):
            return False
        dirs = path.split("/")
        parent = "/".join(dirs[:-1])
        # print(dirs, parent)
        if len(dirs) == 2 or parent in self.paths:
            if path in self.paths:
                return False
            self.paths[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        return self.paths[path] if path in self.paths else -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)