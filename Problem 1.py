'''
1. Store the data. 
Here, since the problem asked us to store data in key-value pairs (our_cache.set(1, 1)), we here use python dictionary (maps) to store the key-value pairs.

2. Keep track of the sequence of new data when added. 
Since python dictionary is not ordered, we can actually use an array because it's good to remove data using specific indexes. 
However, since the problem requires that the time complexity should be O(1), we move to Deque in python, 
see https://www.geeksforgeeks.org/deque-in-python/, which provides an O(1) time complexity for append and pop operations. 

3. When adding new value pairs, step 1 and 2 should be linked together to both change stored values and keep track of the changing sequences.
'''
#Run in a jupyter notebook, python 3.
import collections
class LRU_Cache:
    def __init__(self,capacity):
        self.capacity = capacity # define the capacity of the cache
        self.value = {} # create an empty python dictionary to hold future key-value pairs
        self.key_orders = collections.deque() # https://www.geeksforgeeks.org/deque-in-python/, create an empty deque collection to store the sequence of key.
    def get(self,key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        return self.value.get(key, -1) # https://www.tutorialspoint.com/python/dictionary_get.htm
    def put(self,key,value):
        # Set/put the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        # I think that "to remove the oldest item" means that we could just pop out the first item we added
        if len(self.key_orders) >= self.capacity:
            first = self.key_orders.popleft() # get the key of first item
            print ("! out of cache's capacity, delete first item whose key is ", first)
            del self.value[first] # delete an item in a dictionary, https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary
            self.value[key] = value # add new key-value pairs
            self.key_orders.append(key) # add new key sequence
        else:
            self.value[key] = value # add new key-value pairs
            self.key_orders.append(key) # add new key sequence 

'''Below is the testing process'''
# Instance a cache that has a capacity of 5
our_cache = LRU_Cache(5) 

# Put some key-value pairs:
our_cache.put(1, 1);
our_cache.put(2, 2);
our_cache.put(3, 3);
our_cache.put(4, 4);

# Test 
print (our_cache.get(1))      # returns 1
print (our_cache.get(2))       # returns 2
print (our_cache.get(3))       # returns 3
print (our_cache.get(4))       # returns 4
print (our_cache.get(9))      # returns -1 because 9 is not present in the cache

# Put more values in the cache to test if the cache will remove the first item when cache is full
our_cache.put(5, 5) 
our_cache.put(6, 6)
our_cache.put(7, 6)

# Print current cache
print ("Current cache is ", our_cache.value)
#! out of cache's capacity, delete first item whose key is  1
#! out of cache's capacity, delete first item whose key is  2
#Current cache is  {3: 3, 4: 4, 5: 5, 6: 6, 7: 6}

# Test completed
