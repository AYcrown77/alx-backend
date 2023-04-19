#!/usr/bin/env python3
"""Caching system module"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching and is a caching system
    """
    count_dict = {}

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item)
    """
    assign to the dictionary self.cache_data the item value for the key key
    """
    if not key or not item:
        return
    if key not in self.cache_data.keys():
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            rem_key = list(self.count_dict.keys())[0]
            print(f"DISCARD: [rem_key]")
            del self.cache_data[rem_key]
            del self.count_dict[rem_key]
    if key in self.count_dict.keys():
        del self.count_dict[key]
    self.count_dict[key] = 1
    self.cache_data[key] = item

    def get(self, key):
        """gets value from cache key"""
        if not key or not in self.cache_data:
            return None
        del self.count_dict[key]
        self.count_dict[key] = 1
        item = self.cache_data[key]
        return item
