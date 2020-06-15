def get_largest_sequence_numbers(numbers):
    """
    Solution for getting largest sequence of consecutive numbers
    in given numbers list.
    eg: numbers = [3, 5, 6, 7, 8, 9, 4]
    answer: max length = 5 and range = 5-9
    :param numbers: list of numbers
    :return: tuple of max length and range
    """
    nums = set(numbers)
    min_ele = min(numbers)
    max_ele = max(numbers)

    curr_len = 0
    max_len = 0
    start_num = None
    end_num = None
    new_start_num = None
    for ele in range(min_ele, max_ele+1):
        if curr_len == 0:
            new_start_num = ele
        if ele in nums:
            curr_len += 1
        else:
            if max_len < curr_len:
                start_num = new_start_num
                end_num = ele - 1
                max_len = curr_len
            curr_len = 0
    return max_len, (start_num, end_num)

print(get_largest_sequence_numbers([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))