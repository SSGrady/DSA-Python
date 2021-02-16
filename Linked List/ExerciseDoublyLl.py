class Node:
	def __init__(self, data=None, next=None, prev = None):
		self.data = data
		self.next = next
		self.prev = prev

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.prev = None

	def insert_at_beginning(self, data):
		node = Node(data, self.head, self.prev) #n.data = data, n.next = self.head, n.prev = self.prev
		self.head = node # head = n

	def insert_at_end(self,data):
		if self.head is None:
			self.head = Node(data, None, None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None, itr)

	###############################
	###############################
	###############################
	def print_forward(self):
		# This method prints list in forward direction
		if self.head is None:
			print("Linked List is empty")
			return

		itr = self.head
		llstr = ""
		while itr:
			llstr += str(itr.data) + "-->"
			itr = itr.next
		print (llstr)


	def print_backward(self):
		# Print linked list in reverse direction. Use node.prev for this
		itr = self.head
		rev_llstr = ""
		while itr:
			itr = itr.next
			if itr is None:
				rev_llstr += "<--" + str(itr.prev.data) 
				itr = itr.prev
				break
		while itr:
			rev_llstr += "<--" + str(self.insert_at_beginning(itr.data))
			itr = itr.prev
		print(rev_llstr)

if __name__ == '__main__':
	ll = DoublyLinkedList()
	ll.insert_at_beginning(8)
	ll.insert_at_end(9)
	ll.insert_at_end(10)
	ll.print_forward()
