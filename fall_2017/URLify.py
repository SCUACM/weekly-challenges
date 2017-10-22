# FILE: URLify.py
# AUTH: Tim Shur
# DATE: 10/08/17
# DESC: Solves the URLify weekly challenge. The problem statement is as
#     follows:
#
#     > Write a function to replace all spaces in a string with "%20".
#     > Assume that the string you are given has enough space to hold
#	  > the extra characters, and that you are given the length of the
#	  > text already in the string. String classes are not allowed (use
#	  > a char array).
#
#	  This program was run and tested with Python 2.7.10. To run this
#	  program with all test cases in Terminal in UNIX, for example,
#     enter the following command:
#
#	  $ python URLify.py
#

import unittest

def urlify(string, length):
	"""URL-ify's a given string by replacing spaces with '%20'.

	Note: The Python builtin type `bytearray` is used for this problem
	to avoid the use of immutable string types. The problem statement
	asks to perform this operation in-place, so a bytearray was used to
	simulate a C-style char array. By its nature, bytearray stores the
	character information as bytes (i.e., 'a' becomes 97). Thus, the
	builtin methods `ord` and `chr` are used to switch between
	characters and byte values, where ord('a') = 97 and chr(97) = 'a'.
	If string methods were available, this function would be much
	simpler with Python splicing.

	Args:
		string (str): The original string to be modified. We can assume
			this string has enough space to fit the extra characters.
		length (int): The length of the text in the original string.
			This does not include the extra space needed to fit the
			additional characters.

	Returns:
		str: The URL-ified string with each space replaced by '%20'.

	Examples:
		>>> urlify('I love ACM!    ', 11)
		'I%20love%20ACM!'

		>>> urlify(' Oranges are yummy?      ', 19),
		'%20Oranges%20are%20yummy?'

		>>> urlify('Nospaceshere!', 13)
		'Nospaceshere!'
	"""

	string = bytearray(string)

	# Count spaces in string to find space available
	spaces_count = 0
	for i in xrange(length):
		if chr(string[i]) == ' ':
			spaces_count += 1

	# Begin filling in the string backwards starting from the end
	old_index, new_index = (length - 1), (length + 2*spaces_count - 1)
	
	while old_index < new_index:
		# If space, write '%20' into new section of the string
		# Otherwise, copy the original character and continue
		if chr(string[old_index]) == ' ':
			string[new_index] = ord('0')
			string[new_index - 1] = ord('2')
			string[new_index - 2] = ord('%')
			new_index -= 2
		else:
			string[new_index] = string[old_index]

		new_index -= 1
		old_index -= 1

	return str(string)


class TestURLifyFunction(unittest.TestCase):
	"""Unit testing methods; run by unittest module"""

	def test_case_1(self):
		self.assertEqual(urlify('I love ACM!    ', 11),
						 	    'I%20love%20ACM!')

	def test_case_2(self):
		self.assertEqual(urlify(' Oranges are yummy?      ', 19),
								'%20Oranges%20are%20yummy?')

	def test_case_3(self):
		self.assertEqual(urlify('Nospaceshere!', 13),
								'Nospaceshere!')

	def test_case_4(self):
		self.assertEqual(urlify(' Test URLify function! ! !          ', 26),
				   		 	    '%20Test%20URLify%20function!%20!%20!')

	def test_case_5(self):
		self.assertEqual(urlify(' A B C         ', 7),
						 	    '%20A%20B%20C%20')

	def test_case_6(self):
		self.assertEqual(urlify('               ', 5),
								'%20%20%20%20%20')

	def test_case_7(self):
		self.assertEqual(urlify('Double  space  here              ', 21),
								'Double%20%20space%20%20here%20%20')


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestURLifyFunction)
	unittest.TextTestRunner(verbosity=2).run(suite)
