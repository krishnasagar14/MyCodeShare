class Node(object):
	def __init__(self, node_val):
		self.val = node_val
		self.child_list = []

	def add_child(self, child):
		self.child_list.append(child)


class TreeBoundary(object):
	"""
	Tree boundary problem
	Inspiration: https://www.youtube.com/watch?v=A-OFLt09eZo
	"""
	def __init__(self, root):
		self.root = root

	def get_tree_boundary(self):
		"""
		Tree boundary problem solution with
		modified breath first traversal + stack

		Solution:
		Traverse breath first but for each level get first and last node
		first node goes to result list and last node goes to stack
		After traverse for all levels of tree, empty stack into the result list.
		"""
		res = []
		if not self.root:
			return res
		queue = list()
		stack = list()

		root = self.root
		queue.append(root)
		while queue:
			new_queue_ele = []
			if len(queue) == 1:
				top_ele_node = queue.pop(0)
				res.append(top_ele_node.val)
				new_queue_ele += top_ele_node.child_list
			elif len(queue) > 1:
				f_ele, l_ele = queue[0], queue[-1]
				# make sure that only intermediate levels of tree
				# first and last node is added into result and stack
				# respectively.
				if f_ele.child_list:
					res.append(f_ele.val)
				if l_ele.child_list:
					stack.insert(0, l_ele.val)
				while queue:
					top_ele_node = queue.pop(0)
					if not top_ele_node.child_list:
						# Found child nodes of tree (last level of tree)
						res.append(top_ele_node.val)
					else:
						new_queue_ele += top_ele_node.child_list
			queue += new_queue_ele
		while stack:
			res.append(stack.pop(0))
		return res


root = Node('a')
child_b, child_c = Node('b'), Node('c')
root.add_child(child_b)
root.add_child(child_c)
child_d, child_e, child_f, child_g = Node('d'), Node('e'), Node('f'), Node('g')
child_b.add_child(child_d)
child_b.add_child(child_e)
child_c.add_child(child_f)
child_c.add_child(child_g)
# Tree
"""
   a
 b    c
d e  f g
"""
tb = TreeBoundary(root)
assert(tb.get_tree_boundary() == ['a', 'b', 'd', 'e', 'f', 'g', 'c'])
assert(TreeBoundary(None).get_tree_boundary() == [])
assert(TreeBoundary(Node('a')).get_tree_boundary() == ['a'])
node1 = Node('a')
node1.add_child(Node('b'))
assert(TreeBoundary(node1).get_tree_boundary() == ['a', 'b'])