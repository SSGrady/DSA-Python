# Definition for singly-linked list.
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def megeTwoLists1(self, l1, l2):
		"""
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
		dummy = ListNode()
		tail = dummy
		while l1 and l2:
			if l1.val < l2.val:
				tail.next = l1
				l1 = l1.next
			else:
				tail.next = l2
				l2 = l2.next
			tail = tail.next
		tail.next = l1 or l2
		return dummy.next # l1 = 1-->2-->4,
						  # l2 = 1-->3-->4
						  # dummy.next = 1-->1-->2-->3-->4-->4

		# Dummy.next is the first node in the merged list.
		# Tail.next is the last. Since we want to return the head of the new list, we return dummy.next.
		# in Python everything is considered an object here.
		# When I say tail = dummy, I stored the reference (pointer) for dummy variable
		# into tail. Now every time the tail variable is changed, it'd also affect the dummy variable.