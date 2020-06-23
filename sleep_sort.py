class SleepSort(object):
    """
    Sorting list of positive numbers using multi-threading
    wherein thread will sleep for integer value and
    add integer in result collection.
    These multi-threads will add integers of input list
    in such way that, result contains collection of sorted integers.
    eg: [3, 1, 5, 4, 2]
    for each integer, a new thread will be spawned
    and wait for the same value
    and then, add into result collection
    in such way that result is sorted integers.
    output: [1, 2, 3, 4, 5]
    """
    def __init__(self, arr):
        import time
        self.inp_arr = arr
        self.res = []
        self.time = time
        self.process()

    def __repr__(self):
        return ", ".join(map(str, self.res))

    def add_ele_in_res(self, val):
        """
        Method for adding value to result list
        after delay of input value.
        """
        self.time.sleep(val)
        self.res.append(val)

    def process(self):
        """
        Sorting based on threading each value of input list.
        Logic is based on partition algo of quick sort.
        """
        from threading import Thread

        pivot_ele = self.inp_arr[0]
        part1_arr = []
        part2_arr = []
        for ele in self.inp_arr:
            if ele < pivot_ele:
                part1_arr.append(ele)
            elif ele > pivot_ele:
                part2_arr.append(ele)
        threads = []

        for ele in part1_arr:
            th = Thread(target=self.add_ele_in_res, args=(ele,))
            threads.append(th)
            th.start()
        th = Thread(target=self.add_ele_in_res, args=(pivot_ele,))
        threads.append(th)
        th.start()
        for ele in part2_arr:
            th = Thread(target=self.add_ele_in_res, args=(ele,))
            threads.append(th)
            th.start()
        for th in threads:
            th.join()


print(SleepSort([3, 1, 5, 4, 2]))
print(SleepSort([5, 4, 3, 2, 1]))
print(SleepSort([1, 2, 3, 4, 5]))
print(SleepSort([4, 5, 1, 2, 3]))
print(SleepSort([3, 4, 5, 1, 2]))
