arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def binary_search(arr, target):
    left,right = 0,len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # Target not found


# Example usage
target = 10
result = binary_search(arr, target)
print(f"Target {target} found at index: {result}" if result != -1 else "Target not found")



target = 13

# Now recursive binary search

def recursive_binary_search(arr, target, left, right):
    if left > right:
        return -1  # Target not found
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)  # Search in the right half
    else:
        return recursive_binary_search(arr, target, left, mid - 1)  # Search in the left half
    
    
print("\nRecursive Binary Search:")
result_recursive = recursive_binary_search(arr, target, 0, len(arr) - 1)    
print(f"Target {target} found at index: {result_recursive}" if result_recursive != -1 else "Target not found")