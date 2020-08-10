class InterleavingIterator(object):
	"""
	The interleaving iterator is collection related iterator type
	which iterates over input set of iterators with interleaving manner across all inputs.
	Inspiration: https://techdevguide.withgoogle.com/resources/former-coding-interview-question-flatten-an-iterator-of-iterators/#!

	:param:iter_list: list of iterators
	"""
	def __init__(self, iter_list):
		self.iter_list = iter_list
		self.N = len(self.iter_list)

	def __iter__(self):
		self.curr_iter_index = 0
		return self

	def check_iter_list(self):
		if not self.iter_list:
			raise StopIteration

	def __next__(self):
		self.check_iter_list()
		if self.curr_iter_index >= self.N:
			self.curr_iter_index = 0

		res_val = None
		try:
			res_val = next(self.iter_list[self.curr_iter_index])
			self.curr_iter_index += 1
			return res_val
		except StopIteration:
			self.N -= 1
			self.iter_list.pop(self.curr_iter_index)

		self.check_iter_list()
		if not res_val:
			return self.__next__()


if __name__ == "__main__":
	i1 = iter(range(0))
	i2 = iter(range(5))
	i3 = iter(range(10))

	interleave_iter = InterleavingIterator([i1, i2, i3])
	print([i for i in interleave_iter]) # [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]