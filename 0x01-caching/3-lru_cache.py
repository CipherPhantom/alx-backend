#!/usr/bin/python3
"""
LRUCache Module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represents a cache using LRU algorithm"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            lru_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(lru_key)
            print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
        return self.cache_data.get(key)
