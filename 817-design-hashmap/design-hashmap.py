class ListNode:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
            return
        else:
            curr = self.buckets[index]
            while True:
                if curr.pair[0] == key:
                    curr.pair = (key, value)
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % self.size
        curr = self.buckets[index]
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        curr = self.buckets[index]
        prev = None
        while curr:
            if curr.pair[0] == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.buckets[index] = curr.next
                return
            prev = curr
            curr = curr.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)