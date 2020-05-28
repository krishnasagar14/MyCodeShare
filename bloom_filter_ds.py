# Bloom filter data structure
import hashlib

def hash1(w):
	w = str(w)
	h = hashlib.md5(w.encode())
	return hash(h.hexdigest().encode()[:6])%10

def hash2(w):
	w = str(w)
	h = hashlib.sha256(w.encode())
	return hash(h.hexdigest().encode()[:6])%10

class BloomFilter(object):
	def __init__(self, vector_size, no_of_hashes):
		self.vector_size = vector_size
		self.no_of_hashes = no_of_hashes
		self.vector = [0] * self.vector_size
		self.count = 0
		self.hash_functions = [hash1, hash2]
		if self.no_of_hashes > len(self.hash_functions):
			raise Exception("Number of hashes not supported")

	def insert(self, key):
		hashes = []
		for i in range(self.no_of_hashes):
			hash_func = self.hash_functions[i]
			hash_out = hash_func(key) % self.vector_size
			self.vector[hash_out] = 1
		self.count += 1

	def search(self, key):
		hashes = []
		for i in range(self.no_of_hashes):
			hash_func = self.hash_functions[i]
			hashes.append(hash_func(key) % self.vector_size)
		for h in hashes:
			if self.vector[h] == 0:
				return False
		prob = (1.0 - ((1.0 - 1.0/self.vector_size)**(self.no_of_hashes*self.count))) **self.no_of_hashes
		return "Probability of present = {prob}".format(prob=prob)


bf = BloomFilter(10, 2)
bf.insert(4567)
bf.insert(567)
bf.insert(0)
bf.insert(-1)
print(bf.search(-1))
print(bf.search(0))
print(bf.search("skd"))
print(bf.search(7))
