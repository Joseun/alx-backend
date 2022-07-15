#!/usr/bin/python3
""" Module for LIFO Caching System """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache defines:
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
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)
        return None

    def get(self, key=None):
        """ Get an item from the cache memory """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
