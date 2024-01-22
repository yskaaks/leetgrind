class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = collections.deque()
    def next(self, val: int) -> float:
        self.window.append(val)
        if len(self.window) > self.size:
            self.window.popleft()
            return (sum(self.window)) / self.size
        return (sum(self.window)) / len(self.window)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)