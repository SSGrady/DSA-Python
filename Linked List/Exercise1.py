class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next #represents an individual class of a LinkedList

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data, self.head) #n.value = data , n.next = head
		self.head = node #head = n *
						 #basically redirecting pointers!!
	def print(self):
		if self.head is None:
			print("LinkedList is empty")
			return
			# itr = iterable == current
		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data) + '-->'
			itr = itr.next

		print(llstr)

	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(data, None)

	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count+=1
			itr = itr.next

		return count

	def remove_at(self, index):
		if index < 0 or index >= self.get_length():
			raise Exception("Invalid index")

		if index == 0:
			self.head = self.head.next
			return

		count = 0

		itr = self.head
		while itr:
			if count == index -1:
				itr.next = itr.next.next 
				break # 20:19 - 20:23
			itr = itr.next
			count +=1


	def insert_at(self, index, data):
		if index< 0 or index>self.get_length():
			raise Exception('Invalid Index')
		if index==0:
			self.insert_at_beginning(data)
			return
		count = 0
		itr = self.head
		while itr:
			if count == index -1:
				node = Node(data, itr.next) #you are at the previous element so sneak in between
				itr.next = node
				break

			itr = itr.next
			count +=1

	def find_and_print(self, value):
		itr = self.head
		count = 0
		while itr:
			if itr.data == value:
				return count
				break
			itr = itr.next
			count+=1

	def insert_after_value(self, data_after, data_to_insert):
		# Search for first occurance of data_after in linked list
		# Now insert data_to_insert after data_after node
		if self.head is None:
			return
		itr = self.head
		count = 0
		while itr:
			if itr.data == data_after:
				self.insert_at(count+1, data_to_insert)
				break
			itr = itr.next
			count+=1

	def remove_by_value(self, data):
		# Remove first node that contains data
		if self.head is None:
			return
		itr = self.head
		count = 0
		while itr:
			if itr.data == data:
				self.remove_at(count)
				break
			itr = itr.next
			count+=1


if __name__ == '__main__':
	ll = LinkedList()
	ll.insert_values(["banana","mango","grapes","orange"])
	ll.print()
	ll.insert_after_value("mango","apple") # insert apple after mango
	ll.print()
	ll.remove_by_value("orange") # remove orange from linked list
	ll.print()
	ll.remove_by_value("figs")
	ll.print()
	ll.remove_by_value("banana")
	ll.remove_by_value("mango")
	ll.remove_by_value("apple")
	ll.remove_by_value("grapes")
	ll.print()