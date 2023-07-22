class Hashtable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        raise KeyError(f"Key '{key}' not found.")

    def has(self, key):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return True
        return False

    def keys(self):
        keys_list = []
        for bucket in self.table:
            for kvp in bucket:
                keys_list.append(kvp[0])
        return keys_list

    def hash(self, key):
        return self._hash(key)
