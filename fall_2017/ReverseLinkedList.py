# FILE: ReverseLinkedList.py
# AUTH: Tim Shur
# DATE: 10/13/17
# DESC: Solves the ReverseLinkedList weekly challenge. The problem
#     statement is as follows:
#
#     > Reverse a linked list. For example, given the linked list
#	  > 3 -> 2 -> 1 -> None,
#	  > modify the list so that it becomes
#	  > 1 -> 2 -> 3 -> None.
#
#	  A basic and concise linked list implementation is provided in
#     this file for testing with the reverse_list() function.
#
#     This program was run and tested with Python 2.7.10. To run this
#	  program with all test cases in Terminal in UNIX, for example,
#     enter the following command:
#
#	  $ python ReverseLinkedList.py
#

import unittest

def reverse_list(linked_list):
	"""Reverses the linked list given as an argument.

	Note: A helper method is defined within this function to perform
		the recursion which actually reverses the linked list. The
		reverse_list() function calls this helper function to perform
		the reversal, and then resets the linked_list head to the
		correct node.

	Args:
		linked_list (obj LinkedList): The linked list to be reversed.
			This is an object of the LinkedList class defined in this
			file.

	Returns:
		None: The linked list is reversed in place. No return value
			is specified to reinforce that the original list was
			modified.

	Examples:
		>>> print(linked_list_1)
		'Node(3)->Node(2)->Node(1)->None'
		>>> reverse_list(linked_list_1)
		>>> print(linked_list_1)
		'Node(1)->Node(2)->Node(3)->None'
	"""

	def reverse_helper(head):
		if head is None:
			return

		reverse_helper(head.get_next())

		if head.get_next() is not None:
			(head.get_next()).set_next(head)
			head.set_next(None)

	last_node = linked_list.get_last_node()
	reverse_helper(linked_list.get_head())
	linked_list.set_head(last_node)


class LinkedListNode:
	"""Basic class implementing a Linked List Node."""

	def __init__(self, init_data=0, init_next=None):
		self.data = init_data
		self.next = init_next

	def __str__(self):
		return "Node(" + str(self.data) + ")"

	def set_data(self, data):
		self.data = data

	def set_next(self, node):
		self.next = node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next


class LinkedList:
	"""Basic class implementing a Linked List."""

	def __init__(self):
		self.head = None
		self.count = 0

	def __str__(self):
		result = ""

		current = self.head
		while current:
			result += str(current) + "->"
			current = current.get_next()
		result += "None"

		return result

	def __len__(self):
		return self.count

	def insert(self, data):
		self.head = LinkedListNode(data, self.head)
		self.count += 1
		return data

	def append(self, data):
		current = self.head
		if not current:
			return self.insert(data)

		while current.get_next():
			current = current.get_next()
		current.set_next(LinkedListNode(data, None))
		self.count += 1
		return data

	def delete(self, data):
		previous = current = self.head
		if current and current.get_data() == data:
			return self.delete_head()

		while current:
			if current.get_data() == data:
				previous.set_next(current.get_next())
				self.count -= 1
				return data

			previous, current = current, current.get_next()

		return None

	def set_head(self, new_head):
		self.head = new_head

	def get_head(self):
		return self.head

	def get_last_node(self):
		current = self.head

		while current and current.get_next():
			current = current.get_next()

		return current


class TestReverseLinkedListFunction(unittest.TestCase):
	"""Unit testing suite; implemented in the unittest module"""

	def setUp(self):
		self.linked_list = LinkedList()

	def test_case_0(self):
		reverse_list(self.linked_list)
		self.assertEqual(str(self.linked_list), 'None')

	def test_case_1(self):
		self.linked_list.insert(0)
		reverse_list(self.linked_list)
		self.assertEqual(str(self.linked_list), 'Node(0)->None')

	def test_case_2(self):
		for i in range(2):
			self.linked_list.insert(i)
		reverse_list(self.linked_list)
		self.assertEqual(str(self.linked_list), 'Node(0)->Node(1)->None')

	def test_case_3(self):
		for i in range(3):
			self.linked_list.insert(i)
		reverse_list(self.linked_list)
		self.assertEqual(str(self.linked_list), 'Node(0)->Node(1)->Node(2)->None')

	def test_linked_list(self):
		for i in range(3):
			self.linked_list.insert(i)
		self.assertEqual(str(self.linked_list), 'Node(2)->Node(1)->Node(0)->None')


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseLinkedListFunction)
	unittest.TextTestRunner(verbosity=2).run(suite)
