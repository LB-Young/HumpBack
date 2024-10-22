import uuid


class OrcaCache:
    def __init__(self):
        self.cache = {}

    def get(self, content):
        key = str(uuid.uuid5(uuid.NAMESPACE_DNS, content))
        return self.cache.get(key, None)

    def set(self, content, value):
        key = str(uuid.uuid5(uuid.NAMESPACE_DNS, content))
        self.cache[key] = value

    def delete(self, content):
        key = str(uuid.uuid5(uuid.NAMESPACE_DNS, content))
        del self.cache[key]

    def clear(self):
        self.cache.clear()

    def keys(self):
        return self.cache.keys()

    def values(self):
        return self.cache.values()
    
orcacache = OrcaCache()