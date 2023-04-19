#!/usr/bin/env python3
"""
caching system module
"""


BaseCaching = __import__('base_catching').BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """initializeation"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is none or key not in self.cache_data:
            return
        item = self.cache_data[key]
        return item