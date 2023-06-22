class MyStack:

    def __init__(self):
        self.queue_in = deque()
        
        

    def push(self, x: int) -> None:
        self.queue_in.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.queue_in)-1):
            self.queue_in.append(self.queue_in.popleft())
        return self.queue_in.popleft()
        

    def top(self) -> int:
        return self.queue_in[-1]
        

    def empty(self) -> bool:
        return not self.queue_in
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()