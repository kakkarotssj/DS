class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)

def search(root, val):
	if root is None:
		return None
	else:
		if root.data == val:
			return root
		elif root.data < val:
			return search(root.right, val)
		else:
			return search(root.left, val)


node = search(root, 13)
if not node:
	print "Node doesn't exist."
else:
	print "Node exists"