#!/usr/bin/env python3
"""
Caching system module
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        for the key key
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                rem_key, rem_value = self.cache_data.popitem()
                print(f"DISCARD: {rem_key}")
            self.cache_data[key] = item

    def get(self, key):
        """gets value from cache key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
