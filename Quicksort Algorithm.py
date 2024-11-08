def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    middle = low + (high - low) // 2
    pivot = arr[middle]
    arr[middle], arr[high] = arr[high], arr[middle]  # Move pivot to end
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    return i + 1

# Example usage
words = ["banana", "apple", "cherry", "date"]
quicksort(words, 0, len(words) - 1)
print("Sorted words:", words)
