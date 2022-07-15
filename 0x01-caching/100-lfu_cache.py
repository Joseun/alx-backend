#!/usr/bin/python3
""" Module for LFU Caching System """
import queue
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache defines:
      - constants of your caching system with MAX_ITEMS
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initialize"""
        super().__init__()
        self.queue = {}
        self.count = {}

    def put(self, key=None, item=None):
        """Add an item to the cache memory"""
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                self.queue[key] = len(self.queue)
                self.count[key] = 1
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                lowest_count = self.count.get(list(self.count)[-1])
                least_used = list(self.count)[-1]
                for k, v in self.count.items():
                    if v < lowest_count:
                        lowest_count = v
                        least_used = k
                common_freq = {k: v for k, v in self.count.items()
                               if v == lowest_count}
                if len(common_freq) > 1:
                    temp = {}
                    for k, v in common_freq.items():
                        temp[k] = self.queue.get(k)
                    lru = temp.get(list(temp)[-1])
                    for k, v in self.queue.items():
                        if k in common_freq:
                            if v < lru:
                                lru = v
                    for k, v in self.queue.items():
                        if v == lru:
                            pop_key = k
                        else:
                            self.queue[k] = self.queue[k] - 1
                    self.cache_data.pop(pop_key)
                    self.queue.pop(pop_key)
                    self.count.pop(pop_key)
                    print("DISCARD: {}".format(pop_key))
                    self.queue[key] = len(self.queue)
                    self.count[key] = 1
                else:
                    self.cache_data.pop(least_used)
                    self.count.pop(least_used)
                    self.queue.pop(least_used)
                    print("DISCARD: {}".format(least_used))
                    self.count[key] = 1
                    self.queue[key] = len(self.queue) - 1
                    for k, v in self.queue.items():
                        if v < len(self.queue) - 1:
                            self.queue[k] = self.queue[k] - 1
            if key in self.cache_data:
                self.count[key] = self.count[key] + 1
                old_val = self.queue.get(key)
                if old_val is not None:
                    for k, v in self.queue.items():
                        if v > old_val:
                            self.queue[k] = self.queue[k] - 1
                self.queue[key] = len(self.queue) - 1
            self.cache_data[key] = item
        return None

    def get(self, key=None):
        """Get an item from cache memory"""
        if key and key in self.count:
            self.count[key] = self.count[key] + 1
            old_val = self.queue.get(key)
            if old_val is not None:
                for k, v in self.queue.items():
                    if v > old_val:
                        self.queue[k] = self.queue[k] - 1
                self.queue[key] = len(self.queue) - 1
            return self.cache_data.get(key)
        return None
