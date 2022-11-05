# Databricks notebook source

# import src.sorting as s
# print(s)
# from src.sorting import bubbleSort, selectionSort

# Whoops I'm dumb
from src.sorting.sorting import bubbleSort, selectionSort

class TestClass:
    inp1 = [1, 2, 3, 4, 5] # testing if the methods can receive and return values
    inp2 = [5, 4, 3, 2, 1] # testing if the method can sort 
    expect = [1, 2, 3, 4, 5] # This should be the answer for both tests

    def test1(self):
        bubbleSort(self.inp1)
        assert self.inp1 == self.expect


    def test2(self):
        selectionSort(self.inp2)
        assert self.inp2 == self.expect

# print(test1(inp1, expect))
# print(test1(inp2, expect))

# print(test2(inp1, expect))
# print(test2(inp2, expect))

# Expected output
# True
# True
# True
# True

# Reconfigured this file to be "pytest" compatible