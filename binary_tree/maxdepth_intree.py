class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def findmax_depth(root):
	if not root:
		return 0
	else:
		return 1 + max(findmax_depth(root.left), findmax_depth(root.right))

ans = findmax_depth(root)
print ans