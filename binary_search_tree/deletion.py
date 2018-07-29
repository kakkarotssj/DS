class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BSTree:
	def __init__(self):
		self.root = None

	def _util_insertnode(self, cur_node, data):
		if self.root is None:
			self.root = Node(data)
		else:
			if cur_node is None:
				cur_node = Node(data)
			else:
				if cur_node.data > data:
					if cur_node.left is None:
						cur_node.left = Node(data)
					else:
						self._util_insertnode(cur_node.left, data)
				elif cur_node.data < data:
					if cur_node.right is None:
						cur_node.right = Node(data)
					else:
						self._util_insertnode(cur_node.right, data)

	def insertnode(self, data):
		cur_node = self.root

		self._util_insertnode(cur_node, data)

	def _util_find_parent(self, parent_node, required_node):
		if parent_node.left == required_node:
			return parent_node, "left"
		elif parent_node.right == required_node:
			return parent_node, "right"
		else:
			if parent_node.data > required_node.data:
				return self._util_find_parent(parent_node.left, required_node)
			elif parent_node.data < required_node.data:
				return self._util_find_parent(parent_node.right, required_node)

	def _find_parent(self, cur_node):
		parent_node = self.root

		return self._util_find_parent(parent_node, cur_node)

	def _no_of_children(self, cur_node):
		if cur_node.left and cur_node.right:
			return 2
		elif not cur_node.left and not cur_node.right:
			return 0
		return 1

	def _util_find_successor_node(self, cur_node):
		if cur_node.left:
			return self._util_find_successor_node(cur_node.left)
		
		return cur_node

	def _find_successor_node(self, cur_node):
		child_children_count = self._no_of_children(cur_node.right)
		if child_children_count == 0:
			return cur_node.right
		else:
			if child_children_count == 1:
				if cur_node.right.left is None:
					return cur_node.right
				else:
					return self._util_find_successor_node(cur_node.right)
			else:
				return self._util_find_successor_node(cur_node.right)

	def _util_deletenode(self, cur_node, data):
		if cur_node.data == data:
			children_count = self._no_of_children(cur_node)
			if children_count == 0:
				parent_node, side = self._find_parent(cur_node)
				if side == "left":
					parent_node.left = None
				elif side == "right":
					parent_node.right = None
			elif children_count == 1:
				if cur_node.data == self.root.data:
					if cur_node.right is None:
						self.root = self.root.left
					else:
						self.root = self.root.right
				else:
					if cur_node.left:
						cur_node.data = cur_node.left.data
						child_children_count = self._no_of_children(cur_node.left)
						if child_children_count == 0:
							cur_node.left = cur_node.right = None
						else:
							if not cur_node.left.left:
								cur_node.left = cur_node.left.left
							else:
								cur_node.left = cur_node.left.right
					else:
						cur_node.data = cur_node.right.data
						child_children_count = self._no_of_children(cur_node.right)
						if child_children_count == 0:
							cur_node.left = cur_node.right = None
						else:
							if not cur_node.right.left:
								cur_node.right = cur_node.right.left
							else:
								cur_node.right = cur_node.right.right
			else:
				successor_node = self._find_successor_node(cur_node)
				parent_node, side = self._find_parent(successor_node)
				cur_node.data = successor_node.data
				if side == "left":
					parent_node.left = None
				else:
					parent_node.right = None
		else:
			if data < cur_node.data:
				self._util_deletenode(cur_node.left, data)
			elif data > cur_node.data:
				self._util_deletenode(cur_node.right, data)
		

	def deletenode(self, data):
		cur_node = self.root

		if cur_node.data == data:
			if self._no_of_children(cur_node) == 0:
				self.root = None
			else:
				self._util_deletenode(cur_node, data)
		else:
			if data < cur_node.data:
				cur_node = cur_node.left
				self._util_deletenode(cur_node, data)
			elif data > cur_node.data:
				cur_node = cur_node.right
				self._util_deletenode(cur_node, data)

	def _inorder_traversal(self, root):
		if root is None:
			print "Tree is empty"
		else:
			if root.left:
				self._inorder_traversal(root.left)

			print root.data,
			
			if root.right:
				self._inorder_traversal(root.right)

	def print_tree(self):
		self._inorder_traversal(self.root)

bst = BSTree()
node_values = [50, 30, 20, 40, 70, 60, 80]
for val in node_values:
	bst.insertnode(val)

print "Inorder traversal of given binary search tree ==> ",
bst.print_tree()
print ""

bst.deletenode(20)
print "Inorder traversal of modified tree ==> ",
bst.print_tree()
print ""

bst.deletenode(30)
print "Inorder traversal of modified tree ==> ",
bst.print_tree()
print ""

bst.deletenode(50)
print "Inorder traversal of modified tree ==> ",
bst.print_tree()
print ""
