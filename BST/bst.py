class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# insert new node into tree
def insert(node, val):
	if node is None:
		root = Node(val)
		return root

	if node.data > val:
		if node.left is not None:
			insert(node.left, val)
		else:
			node.left = Node(val)
	else:
		if node.right is not None:
			insert(node.right, val)
		else:
			node.right = Node(val)


# print tree in-order (values to be ascending)
def in_order(root):
	if root is None:
		return

	in_order(root.left)
	print(root.data)
	in_order(root.right)

def pre_order(root):
	if root is None:
		return

	print(root.data)
	pre_order(root.left)
	pre_order(root.right)


R = Node(3)
insert(R, 4)
insert(R, 2)
insert(R, 8)
insert(R, 10)
insert(R, 1)
insert(R, 6)

in_order(R)