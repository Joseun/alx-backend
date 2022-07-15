#!/usr/bin/python3
""" Module for Basic Caching System """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache defines:
      - constants of your caching system with no limits
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initialize"""
        super().__init__()

    def put(self, key=None, item=None):
        """ Add an item to the cache memory """
        if key and item:
            self.cache_data[key] = item
        return None

    def get(self, key=None):
        """ Get an item from cache memory """
        if key:
            return self.cache_data.get(key)
        return None
