class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru_keys = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_keys.remove(key)
            self.lru_keys.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru_keys.remove(key)
        elif len(self.cache) >= self.capacity:
            last_key = self.lru_keys.pop(0)
            del self.cache[last_key]

        self.cache[key] = value
        self.lru_keys.append(key)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)