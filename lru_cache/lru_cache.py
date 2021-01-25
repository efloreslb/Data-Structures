import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
 
        # if key in self.storage:
        #     value = self.storage[key]
        #     self.list.move_to_front(value)
        # else: 
        #     return None

        # if key in self.storage:
        #     value = self.storage[key]
        #     self.cache.move_to_front([key, value])
        # else: return None

        if key not in self.storage:
            return None

        node = self.storage[key]
        self.cache.move_to_front(node)
        return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        # if self.storage.length >= self.limit:
        #     self.storage.remove_from_tail()

        # self.storage.length += 1
        # self.storage.add_to_head({key: value})
        # print({key: value})

        # self.list.add_to_head({key, value})
        # self.storage[key] = self.list.head
        # self.size += 1
        
        # if self.list.length >= self.limit:
        #     self.list.remove_from_tail()
        #     self.storage.pop(self.list.tail)

        # kv = [key, value]

        # if self.size < self.limit:
        #     self.cache.add_to_head(kv)
        #     self.storage[key] = value
        #     self.size += 1

        # if self.size >= self.limit:
        #     self.cache.remove_from_tail()

        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.cache.move_to_front(node)
            return

        if self.size >= self.limit:
            del self.storage[self.cache.tail.value[0]]
            self.cache.remove_from_tail()
            self.size -= 1

        self.cache.add_to_head((key, value))
        self.storage[key] = self.cache.head
        self.size += 1

        
           


        

# cache = LRUCache(3)

# cache.set('item1', 'a')
# cache.set('item2', 'b')
# cache.set('item3', 'c')
# cache.set('item2', 'z')

# print(cache)
# res = cache.get('item1')