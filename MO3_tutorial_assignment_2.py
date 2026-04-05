def find_smallest_index(arr, k):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == k:
            result = mid      # Record match
            high = mid - 1    # Continue searching left for smaller index
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    return result

# Example Usage
arr = [1, 2, 3, 4, 4, 4, 5]
k = 4
print(find_smallest_index(arr, k))  # Output: 3