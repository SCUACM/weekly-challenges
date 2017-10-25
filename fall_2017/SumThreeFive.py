# FILE: SumThreeFive.py
# AUTH: Tim Shur
# DATE: 10/17/17
# DESC: Solves the SumThreeFive weekly challenge. The problem
#     statement is as follows:
#
#     > The positive numbers below 10 which are multiples of 3 or 5
#	  > are 3, 5, 6, and 9. The sum of these multiples is 23. Write
#	  > a function which returns the sum of all multiples of 3 or 5
#     > below 1,000,000.
#
#	  This function uses the closed-form summation of the numbers
#	  of the numbers from 1 to n in order to reduce the runtime
#     complexity to O(1).
#
#     This program was run and tested with Python 2.7.10. To run this
#	  program with all test cases in Terminal in UNIX, for example,
#     enter the following command:
#
#	  $ python SumThreeFive.py
#

import unittest
from math import floor

def sum_three_five(n):
	"""Calculates the sum of the multiples of 3 or 5 up to n.

	This solution uses the mathematical fact that the sum of the
	integers from 1 to n is (n + 1) * n / 2. When we sum the
	multiples of 3 or 5, we must make sure to remove the multiples
	of 15 because they are doubly-counted.

	Args:
		n (int): The upper limit to sum until.

	Returns:
		int: sum of multiples of three or five to n

	Examples:
		>>> print(sum_three_five(1000000))
		233333166668
	"""

	n = n - 1
	three_limit = n // 3
	five_limit = n // 5
	fifteen_limit = n // 15

	three_sum = three_limit * (three_limit + 1) / 2
	five_sum = five_limit * (five_limit + 1) / 2
	fifteen_sum = fifteen_limit * (fifteen_limit + 1) / 2

	return 3*three_sum + 5*five_sum - 15*fifteen_sum


class TestSumThreeFiveFunction(unittest.TestCase):
	"""Run test cases; uses the module unittest"""

	def test_case_1(self):
		self.assertEqual(sum_three_five(10), 23)

	def test_case_2(self):
		self.assertEqual(sum_three_five(1000), 233168)

	def test_case_3(self):
		self.assertEqual(sum_three_five(10000), 23331668)

	def test_case_4(self):
		self.assertEqual(sum_three_five(1000000), 233333166668)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSumThreeFiveFunction)
	unittest.TextTestRunner(verbosity=2).run(suite)
