#!/usr/bin/env python3
"""Caching system module"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialization"""
        super().__init__()
        self.use_keys = []

    def put(self, key, item):
    """
    assign to the dictionary self.cache_data the item value for the key key
    """
    if key is not None and item is not None:
        self.cache_data[key] = item
        if key is not in self.use_keys:
            self.use_keys.append(key)
        else:
            self.use_keys.append(
                self.use_keys.pop(self.use_keys.index(key)))

        if len(self.use_keys) >  BaseCaching.MAX_ITEMS:
            rem_key = self.use_keys.pop(0)
            del self.cache_data[rem_key]
            print(f"DISCARD: [rem_key]")

    def get(self, key):
        """gets value from cache key"""
        if key is not None and key in  self.cache_data.key():
            self.use_keys.append(self.use_keys.pop(self.use_keys.index(key)))
            return self.cache_data[key]
        return None
