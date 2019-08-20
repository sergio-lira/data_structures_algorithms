from collections import OrderedDict

#Created a custom OrderedDict that will always keep new entries at the end of the structure.
# the default behavior is overwriting a value of OrderedDict will keep the new value in the
# positions of the old one, for LRU we want to 'pop' that value and move the new one to the end.
class LRU_Cache():

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def __str__(self):
        s = "<Cache State>\n  key  value\n"

        for key, value in self.cache.items():
            s += f"   {key}--->{value}\n"

        if len(self.cache):
            s += f"last used value: {next(iter(self.cache))}\n"
        else:
            s += '--Empty--'
        return s


    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            #this get operation counts as a cache access so we move the key to the 'bottom'
            self.cache.move_to_end(key)
            return value
        else:
            return -1

    def set(self, key, value):
        if self.capacity  == 0:
            return
        self.cache[key] = value
        #check if adding the last entry put the dict over capacity
        if len(self.cache) > self.capacity:
            #get reference to least_used value and delete it, in this dict it is at the 'top'
            self.cache.popitem(last=False)

print('\n<<< Test Case 1 >>>')
cache = LRU_Cache(5)

cache.set(1, 1);
print(cache)
cache.set(2, 2);
print(cache)
cache.set(3, 3);
print(cache)
cache.set(4, 4);
print(cache)

cache.get(1)       # returns 1
print(cache)
cache.get(2)       # returns 2
print(cache)
cache.get(9)      # returns -1 because 9 is not present in the cache
print(f"get 9: {cache.get(9)}\n")
print(cache)

cache.set(5, 5)
print(cache)
cache.set(6, 6)
print(cache)

cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(f"get 3: {cache.get(9)}\n")

print('\n<<< Test Case 2 >>>')
cache = LRU_Cache(0)
print(cache)
#Prints an empty cache
cache.set('A', 1)
print(cache)
#Won't add the element
cache.get('A')
#Retur -1
print(cache)
cache.set('B', 2)
#Again it wont add the element
print(cache)

print('\n<<< Test Case 3 >>>')
size = 10
cache = LRU_Cache(size)
for n in range(0, size*2):
    cache.set(chr(ord('a')+n), n)
print(cache)
#All elements are new elements, given that we pushed twice the capacity and last value used is n+1

print('\n<<< Test Case 4 >>>')
cache = LRU_Cache(2)
cache.set(1, 1)
cache.set(2, 2)
print(cache)
cache.set(1, 10)
print(cache)
print(cache.get(1))
# should return 10
print(cache.get(2))
# should return 2
print(cache)
