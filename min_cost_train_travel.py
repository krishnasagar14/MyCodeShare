class MinCostForTrainTravel(object):
	"""
	Problem: https://www.geeksforgeeks.org/find-the-minimum-cost-to-reach-a-destination-where-every-station-is-connected-in-one-direction/
	Solution: DP solution
	Time complexity: O(N^2)
	Space complexity: O(N)
	"""
	def __init__(self, costs):
		self.costs = costs

	def get_min_cost(self, start_station, end_station):
		if start_station > end_station:
			return 0
		if start_station == end_station:
			return self.costs[start_station][end_station]

		min_costs = [-1 for _ in range(start_station, end_station + 1)]
		for curr_station in range(end_station - 1, start_station - 1, -1):
			min_cost = self.costs[curr_station][end_station]
			for next_station in range(curr_station + 1, end_station):
				min_cost = min(min_costs[next_station] + self.costs[curr_station][next_station], min_cost)
			min_costs[curr_station] = min_cost
		return min_costs[start_station]

INF = -1
costs = [[0, 15, 80, 90], [INF, 0, 40, 50], [INF, INF, 0, 70], [INF, INF, INF, 0]]
MCTT = MinCostForTrainTravel(costs)
assert(MCTT.get_min_cost(0, len(costs) - 1) == 65)
assert(MCTT.get_min_cost(1, 0) == 0)
assert(MCTT.get_min_cost(1, 2) == 40)