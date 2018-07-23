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

def levelorder_traversal(root):
	queue = [root]
	while queue:
		temp = queue.pop(0)
		print temp.data, 

		if temp.left:
			queue.append(temp.left)
		if temp.right:
			queue.append(temp.right)

print "Level Order traversal for given tree is : ",
levelorder_traversal(root)