class MyHashMap:

    def __init__(self):
        self.keys = []
        self.vals = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.vals.append(value)
        else:
            i = self.keys.index(key)
            self.vals[i] = value

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        i = self.keys.index(key)
        return self.vals[i]

    def remove(self, key: int) -> None:
        if key in self.keys:
            i = self.keys.index(key)
            self.vals.pop(i)
            self.keys.remove(key)
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)