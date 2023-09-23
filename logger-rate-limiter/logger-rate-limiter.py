class Logger:

    def __init__(self):
        self.logger = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logger or self.logger[message] <= timestamp:
            self.logger[message] = timestamp + 10
            return True
        return False
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)