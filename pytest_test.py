from src.sorting.sorting import bubbleSort, selectionSort
import pytest

class TestingClass:
	expect = [1, 2, 3, 4, 5] # This should be the answer for both tests

	# Test 1 - method successfully returns already sorted array
	def test_one(self):
	    arr = [1, 2, 3, 4, 5]
	    bubbleSort(arr)
	    assert arr == self.expect

	# Test 1 - method successfully returns already sorted array
	def test_two(self):
	    arr = [1, 2, 3, 4, 5]
	    selectionSort(arr)
	    assert arr == self.expect

	def test_three(self):
		arr = [5, 4, 3, 2, 1]
		bubbleSort(arr)
		assert arr == self.expect

	def test_four(self):
		arr = [5, 2, 4, 3, 1]
		selectionSort(arr)
		assert arr == self.expect