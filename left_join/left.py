class Hashtable:

  def __init__(self, size=50):
    self.size = size
    self.table = [None] * size

  def set(self, key, value):

    hashkey = self.hash(key)

    if self.table[hashkey] is None:
      self.table[hashkey] = [(key, value)]
    else:
      self.table[hashkey].append((key, value))

  def get(self, key):

    hashkey = self.hash(key)

    return self.table[hashkey]

  def contains(self, key):
 

    hashkey = self.hash(key)

    return self.table[hashkey] is not None

  def keys(self):
 
    keys = []

    for value in self.table:
      if value:
        for pair in value:
          keys.append(pair[0])

    return keys

  

  def hash(self, key):
        hash_value = 5381  
        for char in str(key):
            hash_value = (hash_value * 125457421) + ord(char)%3

        hash_value %= self.size
        return hash_value



def left_join(hashmap1, hashmap2):


  result_hashmap =  Hashtable()

  keys = hashmap1.keys()

  for key in keys:
    if hashmap2.contains(key):
      result_hashmap.set(key, [hashmap1.get(key)[0], hashmap2.get(key)[0]])
    else:
      result_hashmap.set(key, [hashmap1.get(key)[0]])

  return result_hashmap

