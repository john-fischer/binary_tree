class BT_Node():

	def __init__(self, data):
		self.data = data
		self.leftchild = None
		self.rightchild = None
		self.parent = None

class Binary_Tree():

	def __init__(self):
		self.head = None
	#Our insert function

	def tree_append(self, data):
		if self.head == None:
			self.head = BT_Node(data)
			return
		else:
			curr = self.head
			nn = BT_Node(data)
			while True:
				parent = curr
				if curr.data < data and curr.rightchild == None:
					curr.rightchild = nn
					nn.parent = parent
					return
				elif curr.data > data and curr.leftchild == None:
					curr.leftchild = nn
					nn.parent = parent
					return
				elif curr.data < data:
					curr = curr.rightchild
				elif curr.data > data:
					curr = curr.leftchild

	def retrieve_lowest(self):
		if self.head == None:
			return "This binary tree is empty"
		else:
			curr = self.head	
			while curr.leftchild != None:
				curr = curr.leftchild
			return curr.data

	def retrieve_highest(self):
		if self.head == None:
			return "This binary tree is empty"
		else:
			curr = self.head
			while curr.rightchild != None:
				curr = curr.rightchild
			return curr.data


	def remove_lowest(self):
		if self.head.leftchild == None:
			self.head = None
		else:
			parent = self.head
			curr = self.head.leftchild
			while True:
				if curr.leftchild == None:
					parent.leftchild = None
					break
				else:
					parent = curr
					curr = curr.leftchild

	def remove_highest(self):
		if self.head.rightchild == None:
			self.head = None
		else:
			parent = self.head
			curr = self.head.rightchild
			while True:
				if curr.rightchild == None:
					parent.rightchild = None
					return
				else:
					parent = curr
					curr = right.child
	def pop_lowest(self):
		if self.head.leftchild == None:
			self.head = None
			return None
		else:
			parent = self.head
			curr = self.head.leftchild
			while True:
				if curr.leftchild == None:
					parent.leftchild = None
					return curr.data
				else:
					parent = curr
					curr = curr.leftchild

	def pop_highest(self):
		if self.head.rightchild == None:
			self.head = None
			return None
		else:
			parent = self.head
			curr = self.head.rightchild
			while True:
				if curr.rightchild == None:
					parent.rightchild = None
					return curr.data
				else:
					parent = curr
					curr = curr.rightchild





my_tree = Binary_Tree()
my_tree.tree_append(-1)
my_tree.tree_append(-2)
my_tree.tree_append(4)
my_tree.tree_append(6)
my_tree.tree_append(8)
my_tree.tree_append(1)
print(my_tree.head.leftchild.data)
print(my_tree.head.rightchild.data)
print(my_tree.head.leftchild.parent.data)
print(my_tree.head.rightchild.rightchild.data)
print(str(my_tree.retrieve_highest()))
my_tree.remove_lowest()
my_tree.tree_append(-10)
my_tree.tree_append(-2)
print(str(my_tree.retrieve_lowest()))