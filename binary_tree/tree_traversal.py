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


def preorder(root):
	print root.data, 
	if root.left:
		preorder(root.left)
	if root.right:
		preorder(root.right)

print "PREORDER TRAVERSAL ==>",
preorder(root)
print ""


def inorder(root):
	if root.left:
		inorder(root.left)
	print root.data,
	if root.right:
		inorder(root.right)

print "INORDER TRAVERSAL ==>",
inorder(root)
print ""


def postorder(root):
	if root.left:
		postorder(root.left)
	if root.right:
		postorder(root.right)
	print root.data,

print "POSTORDER TRAVERSAL ==>",
postorder(root)
print ""