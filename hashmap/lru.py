from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # Maintains order of insertion

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Key not found
        
        # Move key to end to mark it as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the key so it can be re-added at the end (most recently used)
            self.cache.move_to_end(key)
        
        self.cache[key] = value  # Insert or update key-value pair

        if len(self.cache) > self.capacity:
            # Remove the first inserted (least recently used) item
            self.cache.popitem(last=False)

# Usage example
lru = LRUCache(3)
lru.put(1, 10)  # Cache: {1: 10}
lru.put(2, 20)  # Cache: {1: 10, 2: 20}
lru.put(3, 30)  # Cache: {1: 10, 2: 20, 3: 30}

print(lru.get(1))  # Output: 10 (Cache: {2: 20, 3: 30, 1: 10})
lru.put(4, 40)     # Cache: {3: 30, 1: 10, 4: 40} (2 is removed)
print(lru.get(2))  # Output: -1 (2 was evicted)
print(lru.get(3))  # Output: 30
