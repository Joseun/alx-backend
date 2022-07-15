#!/usr/bin/python3
""" Module for LRU Caching System """
import queue
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache defines:
      - constants of your caching system with MAX_ITEMS
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initialize"""
        super().__init__()
        self.queue = {}

    def put(self, key=None, item=None):
        """Add an item to the cache memory"""
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                self.queue[key] = len(self.queue)
            elif len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                for k, v in self.queue.items():
                    if v == 0:
                        pop_key = k
                    else:
                        self.queue[k] = self.queue[k] - 1
                self.cache_data.pop(pop_key)
                self.queue.pop(pop_key)
                print("DISCARD: {}".format(pop_key))
                self.queue[key] = len(self.queue)
            if key in self.cache_data:
                old_val = self.queue.get(key)
                for k, v in self.queue.items():
                    if v > old_val:
                        self.queue[k] = self.queue[k] - 1
                self.queue[key] = len(self.queue) - 1
            self.cache_data[key] = item
        return None

    def get(self, key=None):
        """Get an item from cache memory"""
        if key:
            old_val = self.queue.get(key)
            if old_val:
                for k, v in self.queue.items():
                    if v > old_val:
                        self.queue[k] = self.queue[k] - 1
                self.queue[key] = len(self.queue) - 1
            return self.cache_data.get(key)
        return None
