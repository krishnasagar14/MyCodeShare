def get_next_prime(n):
	if n <=2:
		return 2
	is_found = False
	while(not is_found):
		if (n % 2 != 0 or n % 3 != 0):
			tmp_n = n
			for i in range(5, int(tmp_n ** 0.5), 6):
				if tmp_n % i != 0 or tmp_n % (i +2) != 0:
					is_found = True
				else:
					is_found = False
		n += 1
	return n

class RollingHash(object):
	"""
	Rolling hash data structure using for finding patterns in string matching problems
	"""
	def __init__(self, inp_str):
		self.s = inp_str
		self.l = len(self.s)
		self.m = get_next_prime(self.l)

	def get_hash_for_substr(self, sub_str_len):
		hashes = []
		i = 0
		while i < self.l:
			if i == 0:
				sub_str = self.s[i:i+sub_str_len]
				h_val = 0
				mx_len = sub_str_len - 1
				for s in sub_str:
					h_val += (self.m ** mx_len) * ord(s)
					mx_len -= 1
				hashes.append(h_val)
			else:
				prev_s = self.s[i - 1]
				next_s = self.s[i]
				prev_hash = hashes[-1]
				prev_s_h = ord(prev_s) * (self.m ** (sub_str_len - 1))
				next_s_h = ord(next_s)
				new_hash = prev_hash - prev_s_h + next_s_h
				hashes.append(new_hash)
			i += 1
		return hashes

s = 'abcd'
s1 = 'bcde'
rh1 = RollingHash(s)
rh2 = RollingHash(s1)
hashes1 = rh1. get_hash_for_substr(2)
hashes2 = rh2.get_hash_for_substr(2)
print(hashes1, hashes2)
