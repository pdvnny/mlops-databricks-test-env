def bubbleSort(arr):
    """
    :param: arr This is an array that needs to be sorted. It is sorted in-place.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):
    """
    :param: arr This is an array that needs to be sorted. It ends up being sorted in-place.
    """
    n = len(arr)
    
    for step in range(n):
        min_idx = step
        
        for i in range(step+1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])
