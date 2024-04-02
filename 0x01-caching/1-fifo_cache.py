#!/usr/bin/python3
"""
FIFOCache Module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents a cache using FIFO algorithm"""

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
            first_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
