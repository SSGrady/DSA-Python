def insertionSort(arr): 
  for i in range(1, len(arr)):
  	key = arr[i]
  	j = i-1
  	while j >= 0 and arr[j]> key:
  		arr[j+1] = arr[j]
  		j -= 1
  		arr[j+1] = key
  return arr


class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def find(self,data):
		itr = self.head
		while itr:
			if itr.data == data:
				break
			itr = itr.next
		return itr.data
	
	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node


	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(data, None)

def main():
	return

if __name__ == '__main__':
	main()
	arr = [5,2,4,6,1,3]
	#print("Sorted array:", insertionSort(arr))
	ll = LinkedList()
	ll.insert_at_beginning(1)
	ll.insert_at_end(2)
	ll.insert_at_end(3)
	ll.insert_at_end(4)
	print("[",ll.head.data, "] -->", "[", ll.find(2), "] -->", "[", ll.find(3), "] -->", "[", ll.find(4), "]")

	