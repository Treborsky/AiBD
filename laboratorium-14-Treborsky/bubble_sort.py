"""Simple bubble sort implementation"""

def bubble_sort(array):
    
    if not array:
        return []

    n = len(array)

    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

