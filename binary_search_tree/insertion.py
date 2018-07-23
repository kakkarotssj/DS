class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def insert(root, node):
	if root.data < node.data:
		if not root.right:
			root.right = node
		else:
			insert(root.right, node)
	elif root.data > node.data:
		if not root.left:
			root.left = node
		else:
			insert(root.left, node)


def inorder_traversal(root):
	if root.left:
		inorder_traversal(root.left)
	print root.data,
	if root.right:
		inorder_traversal(root.right)


root = Node(50)
insert(root,Node(30))
insert(root,Node(20))
insert(root,Node(40))
insert(root,Node(70))
insert(root,Node(60))
insert(root,Node(80))


inorder_traversal(root)