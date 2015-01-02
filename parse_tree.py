from tree_data_structure.py import BinaryTree
from stacks.py import Stack
import operator

### Build a parse tree
### Evaluate infomation in the tree

# Parse a math expression and turn it into a tree.  Can do this with anything and then traverse the tree to find values as needed.
def buildParseTree(mathexp):
	exp_list = mathexp.split()		# Turn the expression into a list of items we will parse through
	p_stack = Stack()				# Create a stack object. Use this to store parent nodes as we move down the tree.
	e_tree = BinaryTree('')			# Create an empty binary tree object.
	p_stack.push(e_tree)			# Go ahead and put the first node, which is a parent node, into the stack.
	current_tree = e_tree 			# Set the 'current' pointer to be on the e_tree

	for item in exp_list:
		# If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
		if item == '(':
			current_tree.insertLeft('')					# Create a node to the left
			p_stack.push(current_tree)					# Keep track of the current node as a parent
			current_tree = current_tree.getLeftChild()	# Descend to the left child just created
		# If the current token is a number, set the root value of the current node to the number and return to the parent.
		elif item not in ['+', '-', '*', '/', ')']:		# If not one of these then the item is a number and therefore a leaf
			current_tree.setRootVal(int(item))			# Set number as the root of the tree
			parent = p_stack.pop()						# Get the parent node
			current_tree = parent						# Go to the parent node
		# If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
		elif item in ['+', '-', '*', '/']:
			current_tree.setRootVal(item)				# Set the operand as the root value
			current_tree.insertRight('')				# Add node to the right
			p_stack.push(current_tree)					# Add node I'm at to the parent node stack before decending to the child
			current_tree = current_tree.getRightChild()
		# If the current token is a ')', go to the parent of the current node.
		elif item == ')':								# We are at the end of the expresion or part of the expression
			current_tree = p_stack.pop()				# Go to the parent node
		else:
			raise ValueError
	return e_tree

parsetree = buildParseTree("( ( 10 + 5 ) * 3 )")

# Evaluate the information in the parse tree
	# Get left and right children of the current node.
	# If no children then it is a leaf node and we return the value of current node.
	# If there is a child, look up the operator and apply to results from recusive evaluation of L and R children

def evaluate(parseTree):
	opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()

	if leftC and rightC:		# If there are a left and right child, we know this is not a leaf node, and hence an operator
		fn = opers[parseTree.getRootVal()]		# Get the root val of the tree I'm in since it will be the operator
		return fn(evaluate(leftC), evaluate(rightC))	# Pass in the values for the function to evaluate, which in this case we can call our function recursively, since eventually we will reach a leaf node consisting of an operand, which will then be evaluated.
	else:
		return parseTree.getRootVal		# Base case of no children, we know it's a leaf node and hence the operand to be evaluated and returned, causing the call function to collapse.
