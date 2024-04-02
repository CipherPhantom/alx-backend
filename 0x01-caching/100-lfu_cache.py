#!/usr/bin/python3
"""
LFUCache Module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents a cache using MRU algorithm"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.count = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        self.cache_data[key] = item
        self.count[key] = 0
        if len(self.cache_data) > self.MAX_ITEMS:
            print(self.count)
            lfu_value = min([v for k, v in self.count.items() if k != key])
            lfu_list = [k for k, v in self.count.items() if v == lfu_value]
            lru_key = [k for k in self.cache_data.keys() if k in lfu_list][0]
            self.cache_data.pop(lru_key)
            self.count.pop(lru_key)
            print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            self.count[key] += 1
        return self.cache_data.get(key)
