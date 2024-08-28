class HashMap:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
