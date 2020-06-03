# To find kth largest sum of contiguous sub-array of given array

def kth_largest_sum_contiguous_array(arr, k):
	l = len(arr)
	m = 0
	n = m + k
	max_sum = 0
	curr_sum = sum(arr[m:n])
	while(n < l):
		max_sum = max(max_sum, curr_sum)
		curr_sum = curr_sum - arr[m] + arr[n]
		m += 1
		n += 1
	return max_sum

arr1 = [-3, 2, 3, -5, 8, 9, -10]
arr2 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kth_largest_sum_contiguous_array(arr1, 4))
print(kth_largest_sum_contiguous_array(arr2, 4))
