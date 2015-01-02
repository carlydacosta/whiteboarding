# These are written as external functions vs methods of the BinaryTree class because I rarely just want to traverse the tree.  Most of the time I will want to accomplish something else while using the traversal pattern.

def preorder(tree):
	if tree:		# First check to make sure there is a tree
		print tree.getRootVal()			# Print the root.  Since not saving the root value, we can just print it vs returning it.
		preorder(tree.getLeftChild())		# Recursive call of the function passing in L child as the tree
		preorder(tree.getRightChild())		# Same with R child

def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print tree.getRootVal()

def inorder(tree):
	if tree != None:
		inorder(tree.getLeftChild())
		print tree.getRootVal()
		inorder(tree.getRightChild())