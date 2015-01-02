# Methods used to build trees
#	1. List of Lists
#	2. Nodes and References

################## list of lists representation ########################

##### tree built from below code ########
# myTree = ['a',		#root
# 			['b',	#left subtree
# 				[],
# 				['d', [], []],
# 			],
# 			['c',	#right subtree
# 				['e', [], []],
# 				['f', [], []]
# 			]
# 		]


def buildTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = buildTree('a')
insertLeft(r,'b')
insertRight(r,'c')
l = getLeftChild(r)
insertRight(l,'d')
rc = getRightChild(r)
insertLeft(rc,'e')
insertRight(rc,'f')
print r


################## Nodes and References ########################

class BinaryTree():
	def __init__(self, rootObj):  # Called the constructor function.  Creates (or initializes) a new object of the BinaryTree class.  Object has:
		self.key = rootObj					# A key (name), represented by a string or int for example
		self.leftChild = None				# A left child reference
		self.rightChild = None				# A right child reference

	### Insertion methods ###
	def insertLeft(self, newNode):
		if self.leftChild == None:					# If current node has no reference to a left child
			self.leftChild = BinaryTree(newNode)	# Then give it one, which will be a tree in itself (or node) with key, left and right attributes as well
		else:
			temp = BinaryTree(newNode)				# If the tree already has a reference to a left child, then we create the child we want to insert and hold it as temp
			temp.leftChild = self.leftChild 		# We assign the current tree's left child to the left child of our temp
			self.leftChild = temp					# Then reassign the new tree held by temp as the left child of the current tree

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.rightChild = self.rightChild
			self.rightChild = temp

	### Accessor methods ###
	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.key = obj

	def getRootVal(self):
		return self.key

