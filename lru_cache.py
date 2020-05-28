class LRUCache(object):
	def __init__(self, max_size=10):
		from collections import OrderedDict
		self.max_size = max_size
		self.data_store = OrderedDict()
		self.store_size = 0

	def get(self, key):
		val = self.data_store.get(key, None)
		if not val:
			return None
		self.data_store.pop(key)
		self.data_store[key] = val
		return val

	def set(self, key, val):
		is_store_full = (self.store_size == self.max_size)
		if is_store_full:
			for first_key in self.data_store.keys():
				self.data_store.pop(first_key)
				break
		self.data_store[key] = val
		self.store_size += 1

	def remove(self, key):
		if key not in self.data_store:
			return None
		self.store_size -= 1
		return self.data_store.pop(key)

	def get_cache_contents(self):
		print("Cache:\n")
		for k, v in self.data_store.items():
			print("{key} : {value}\n".format(key=k, value=v))

cache = LRUCache(max_size=3)
cache.get_cache_contents()
print(cache.get("hfdgkhg"))
cache.set("a", [1, 2, 3])
cache.set("b", "string")
cache.set("c", (23, ))
cache.get_cache_contents()
print(cache.get("a"))
cache.set("d", {"b": "string"})
cache.get_cache_contents()
print(cache.remove("a"))
cache.get_cache_contents()
cache.set("e", "a")
cache.get_cache_contents()
cache.set("f", "b")
cache.get_cache_contents()
