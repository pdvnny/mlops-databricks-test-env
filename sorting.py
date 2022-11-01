# Copyied from Suyash's & Balaji's code on our main repo

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
