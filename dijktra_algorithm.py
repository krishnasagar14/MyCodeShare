class DijktraAlgo(object):
	def __init__(self, vertices):
		self.V = vertices
		self.graph = {}

	def add_weighted_edge(self, n1, n2, wt):
		self.graph.setdefault(n1, {})
		self.graph[n1][n2] = wt
		self.graph.setdefault(n2, {})
		self.graph[n2][n1] = wt

	def process(self, start, dest):
		cost = [None for i in range(self.V)]
		cost[start] = 0
		visited = [0 for i in range(self.V)]
		path = [start]

		min_vertex = start
		while min_vertex != dest:
			visited[min_vertex] = 1
			adjacency = self.graph[min_vertex]
			min_cost = None
			new_min_vertex = None
			for ad_n, wt in adjacency.items():
				if visited[ad_n] == 1:
					continue
				new_wt = cost[min_vertex] + wt
				if cost[ad_n]:
					min_wt = min(new_wt, cost[ad_n])
				else:
					min_wt = new_wt
				if not min_cost:
					min_cost = min_wt
					new_min_vertex = ad_n
				else:
					if min_cost > min_wt:
						min_cost = new_wt
						new_min_vertex = ad_n
				cost[ad_n] = min_wt
			if new_min_vertex:
				min_vertex = new_min_vertex
				path.append(min_vertex)
			if not new_min_vertex:
				break
		if cost[dest]:
			path.append(dest)
			return cost[dest], path
		else:
			return "Not Possible"


DA_short = DijktraAlgo(9)
DA_short.add_weighted_edge(0, 1, 4)
DA_short.add_weighted_edge(0, 7, 8)
DA_short.add_weighted_edge(1, 2, 8)
DA_short.add_weighted_edge(1, 7, 11)
DA_short.add_weighted_edge(2, 3, 7)
DA_short.add_weighted_edge(2, 8, 2)
DA_short.add_weighted_edge(2, 5, 4)
DA_short.add_weighted_edge(3, 4, 9)
DA_short.add_weighted_edge(3, 5, 14)
DA_short.add_weighted_edge(4, 5, 10)
DA_short.add_weighted_edge(5, 6, 2)
DA_short.add_weighted_edge(6, 7, 1)
DA_short.add_weighted_edge(6, 8, 6)
DA_short.add_weighted_edge(7, 8, 7)
print(DA_short.process(0, 4))
print(DA_short.process(1, 6))
