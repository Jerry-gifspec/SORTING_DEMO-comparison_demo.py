from timing_sort_algo import run_sorting_algorithm
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort

numbers_list = [
    10, 82, 6, 18, 37, 21, 58, 45, 93, 76, 12, 89, 67, 23, 91, 78, 56, 43, 30, 27, 
    15, 85, 62, 49, 36, 24, 13, 81, 68, 55, 42, 31, 20, 9, 87, 64, 51, 38, 26, 14, 
    83, 70, 57, 44, 32, 22, 11, 88, 65, 52, 39, 28, 17, 86, 73, 60, 47, 35, 25, 16, 
    90, 77, 63, 50, 37, 26, 15, 84, 71, 59, 46, 34, 23, 12, 91, 78, 66, 53, 41, 30, 
    29, 18, 87, 74, 61, 48, 36, 25, 14, 92, 79, 67, 54, 42, 31, 20, 9, 88, 75, 63, 
    51, 39, 28, 17, 86, 73, 60, 47, 35, 24, 13, 90, 77, 65, 52, 40, 29, 19, 8, 89, 
    76, 64, 53, 41, 30, 27, 16, 91, 78, 66, 54, 43, 32, 21, 10, 87, 75, 62, 50, 38, 
    27, 15, 92, 79, 67, 55, 44, 33, 22, 11, 88, 76, 63, 51, 39, 28, 17, 85, 73, 60, 
    48, 36, 25, 14, 93, 80, 68, 56, 45, 34, 23, 12, 91, 79, 67, 55, 44, 33, 22, 11, 
    89, 77, 65, 53, 42, 31, 20, 9, 88, 76, 64, 52, 41, 30, 29, 18, 87, 75, 63, 51, 
    40, 29, 19, 8, 90, 78, 66, 54, 43, 32, 21, 10, 89, 77, 65, 53, 42, 31, 20, 9, 
    88, 76, 64, 52, 41, 30, 29, 18, 87, 75, 63, 51, 40, 29, 19, 8, 90, 78, 66, 54, 
    43, 32, 21, 10, 89, 77, 65, 53, 42, 31, 20, 9, 88, 76, 64, 52, 41, 30, 29, 18, 
    87, 75, 63, 51, 40, 29, 19, 8, 90, 78, 66, 54, 43, 32, 21, 10, 89, 77, 65, 53, 
    42, 31, 20, 9, 88, 76, 64, 52, 41, 30, 29, 18, 87, 75, 63, 51, 40, 29, 19, 8, 
    90, 78, 66, 54, 43, 32, 21, 10, 89, 77, 65, 53, 42, 31, 20, 9, 88, 76, 64, 52, 
    41, 30, 29, 18, 87, 75, 63, 51, 40, 29, 19, 8, 90, 78, 66, 54, 43, 32, 21, 10, 
    89, 77, 65, 53, 42, 31, 20, 9, 88, 76, 64, 52, 41, 30, 29, 18, 87, 75, 63, 51, 
    40, 29, 19, 8, 90, 78, 66, 54, 43, 32, 21, 10, 89, 77, 65, 53, 42, 89, 77, 65, 
    53, 42
]

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Heap Sort Implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Timsort (Python's built-in sort)
def tim_sort(arr):
    return sorted(arr)

# Example usage with the given list of numbers
numbers = [
    10, 82, 6, 18, 37, 21, 58, 45, 93, 76, 12, 89, 67, 23, 91, 78, 56, 43, 30, 27,
    15, 85, 62, 49, 36, 24, 13, 81, 68, 55, 42, 31, 20, 9, 87, 64, 51, 38, 26, 14,
    83, 70, 57, 44, 32, 22, 11, 88, 65, 52, 39, 28, 17, 86, 73, 60, 47, 35, 25, 16,
    90, 77, 63, 50, 37, 26, 15, 84, 71, 59, 46, 34, 23, 12, 91, 78
]

merge_sorted_numbers = merge_sort(numbers.copy())
heap_sorted_numbers = heap_sort(numbers.copy())
quick_sorted_numbers = quick_sort(numbers.copy())
timsort_sorted_numbers = tim_sort(numbers.copy())

print("\nMerge Sort:\n", merge_sorted_numbers,"\n")
print("\nHeap Sort:\n", heap_sorted_numbers,"\n")
print("\nQuick Sort:\n", quick_sorted_numbers,"\n")
print("\nTimsort:\n", timsort_sorted_numbers,"\n")
