
### Just talking about a stack and what it does is the abstract data type.
### I give an abstract data type a physical representation as a data structure.
### This is building the data structure.
### Make a class to create an object that responds to things we want it to do with methods.

class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)


stack = Stack()
print stack.items
print stack.isEmpty()
stack.push(4)
print stack.items
stack.push('dog')
print stack.items
print stack.peek()
stack.push(True)
print stack.items
print stack.size()
print stack.isEmpty()
stack.push(8.4)
print stack.items
print stack.pop()
print stack.pop()
print stack.size()
