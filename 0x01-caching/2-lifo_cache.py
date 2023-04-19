#!/usr/bin/env python3
"""
Caching system module
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """
    keys_no = []

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        for the key key
        """
        if not key or not item:
            return
        if key in self.cache_data
            self.cache_data[key] = item
            self.keys_no.append(key)
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            rem_key = self.keys_no.pop()
            del self.cache_data[rem_key]
            print(f"DISCARD: {rem_key}")
        self.cache_data[key] = item
        self.keys_no.append(key)

    def get(self, key):
        """gets value from cache key"""
        if not key of key not in self.cache_data:
            return None
        item = self.cache_data[key]
        return item
