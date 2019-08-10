import math
import mmh3 # murmur3 hash function
from bitarray import bitarray
from random import shuffle 

class BloomFilter(object):
    def __init__(self, item_counts, fp_prob):

        # probability of false positives
        self.fp_prob = fp_prob

        # size of bit array
        self.bit_array_size = self.get_size(self.fp_prob, item_counts)

        # number of hash functions to be used
        self.hash_count = self.get_hash_count(self.bit_array_size, item_counts)

        self.bit_array = bitarray(self.bit_array_size)
        self.bit_array.setall(0)

    def add(self, word):
        result_hash = []

        for i in range(self.hash_count):
            hash = mmh3.hash(word, i) % self.bit_array_size

            result_hash.append(hash)
            self.bit_array[hash] = True
        
    def check(self, word):
        for i in range(self.hash_count):
            hash = mmh3.hash(word, i) % self.bit_array_size
            if self.bit_array[hash] == False:
                return False
        return True
    
    def get_size(self, fp_prob, item_counts):
        m = -(item_counts * math.log(fp_prob)) / (math.log(2)**2)
        return int(m)
    
    def get_hash_count(self, size, items_count):
        k = (size/items_count) * math.log(2)
        return int(k)


n = 20 #no of items to add 
p = 0.05 #false positive probability 
  
bloomf = BloomFilter(n,p) 
print("Size of bit array:{}".format(bloomf.bit_array_size)) 
print("False positive Probability:{}".format(bloomf.fp_prob)) 
print("Number of hash functions:{}".format(bloomf.hash_count)) 
  
# words to be added 
word_present = ['abound','abounds','abundance','abundant','accessable', 
                'bloom','blossom','bolster','bonny','bonus','bonuses', 
                'coherent','cohesive','colorful','comely','comfort', 
                'gems','generosity','generous','generously','genial'] 
  
# word not added 
word_absent = ['bluff','cheater','hate','war','humanity', 
               'racism','hurt','nuke','gloomy','facebook', 
               'geeksforgeeks','twitter'] 
  
for item in word_present: 
    bloomf.add(item) 
  
shuffle(word_present) 
shuffle(word_absent) 
  
test_words = word_present[:10] + word_absent 
shuffle(test_words) 
for word in test_words: 
    if bloomf.check(word): 
        if word in word_absent: 
            print("'{}' is a false positive!".format(word)) 
        else: 
            print("'{}' is probably present!".format(word)) 
    else: 
        print("'{}' is definitely not present!".format(word))