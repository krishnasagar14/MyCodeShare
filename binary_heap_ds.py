class BinaryHeap(object):
	def __init__(self, elements):
		self.data_stor = []
		self.stor_len = 0
		for ele in elements:
			self.insert(ele)

	@staticmethod
	def get_child_indexes(idx):
		return 2*idx + 1, 2*idx + 2

	def insert(self, ele):
		self.data_stor.append(ele)
		self.stor_len += 1
		self.min_heap()

	def get_min(self):
		return self.data_stor[0]

	def get_max(self, start=0):
		if self.stor_len <= 3:
			return max(self.data_stor)
		child1_i, child2_i = self.get_child_indexes(start)
		if child2_i >= self.stor_len and child1_i < self.stor_len:
			return self.data_stor[child1_i]
		if child1_i >= self.stor_len and child2_i < self.stor_len:
			return self.data_stor[child2_i]
		if child2_i >= self.stor_len or child1_i >= self.stor_len:
			return self.data_stor[start]
		return max(self.get_max(start=child1_i), self.get_max(start=child2_i))

	def swap(self, i, j):
		self.data_stor[i], self.data_stor[j] = \
			self.data_stor[j], self.data_stor[i]

	def min_heap(self):

		if self.stor_len <= 2:
			return
		i = 0
		while i < self.stor_len:
			child1_i, child2_i = self.get_child_indexes(i)
			if child2_i >= self.stor_len or child1_i >= self.stor_len:
				return
			min_ele = min((self.data_stor[i], 
				self.data_stor[child1_i], self.data_stor[child2_i]))
			min_ele_i = self.data_stor.index(min_ele)
			if min_ele_i != i:
				self.swap(i, min_ele_i)
				i = min_ele_i
			else:
				i += 1

	def print_heap(self):
		print(self.data_stor)

BH = BinaryHeap([34, 2, 1, 35, 67, 6, 4])
print(BH.get_max())
BH.insert(68)
print(BH.get_max())
BH.insert(5)
print(BH.get_max())
BH.print_heap()
