#!/usr/bin/python3
"""
LIFOCache Module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents a cache using LIFO algorithm"""

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
            last_key = list(self.cache_data.keys())[-2]
            self.cache_data.pop(last_key)
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
