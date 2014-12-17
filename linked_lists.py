class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self, data):

		new_node = Node(data)

		if self.head == None:			#if there is no head (ie no list started yet), the new node is the head
			self.head = new_node

		if self.tail:					#if there is a tail:
			self.tail.next = new_node	#before assigning the new node as the new tail, I first have to tell the tail there is something next, which is the new node

		self.tail = new_node			#now I can assign the new node as the new tail

		print "new node:", new_node.data, "head:", self.head.data, "tail:", self.tail.data

	def findNode(self, data):
		
		current = self.head

		while current:
			print "current node:", current.data
			if data == current.data:
				print "found node:", current.data
				return

			else:
				current = current.next
				
		print "No node found."
		return None

	def insertNode(self, before_data, data):

		current = self.head

		new_node = Node(data)

		while current:
			if current.next and current.next.data == before_data:
				print "inserted new node before:", current.next.data
				new_node.next = current.next
				current.next = new_node
				print "inserted node:", new_node.data
				return

			else:
				current = current.next

		print "No node found to insert data ahead of."
		return None

	def deleteNode(self, data):

		current = self.head

		while current:
			if current.next and current.next.data == data:
				print "node to be deleted:", current.next.data
				current.next = current.next.next
				print "new next node:", current.next.next.data
				return
			else:
				current = current.next
		print "No node found to be deleted."
		return None

	def findKFromEnd(self, k):

		p1 = self.head
		p2 = self.head
		count = 0

		while count != k:
			count = count + 1
			p1 = p1.next

		while p1.next:
			p1 = p1.next
			p2 = p2.next

		print k,"node from the end:", p2.data
		return

	def printNodes(self):
		node = self.head

		while node:
			print node.data
			node = node.next
		

linkedlist = LinkedList()

linkedlist.printNodes()

linkedlist.addNode(5)
linkedlist.addNode(7)
linkedlist.addNode(2)
linkedlist.addNode(9)
linkedlist.addNode(11)

linkedlist.findNode(2)

linkedlist.insertNode(11,3)

linkedlist.deleteNode(9)

linkedlist.printNodes()

linkedlist.findKFromEnd(3)