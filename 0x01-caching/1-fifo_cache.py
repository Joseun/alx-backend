#!/usr/bin/python3
""" Module for FIFO Caching System """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache defines:
      - constants of your caching system with MAX_ITEMS
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initialize"""
        super().__init__()
        self.key_indexes = []

    def put(self, key=None, item=None):
        """ Add an item to the cache memory """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key=None):
        """ Get an item from the cache memory """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
