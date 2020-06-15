# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) > 0:
        low = start
        high = end
        mid = (low + high) // 2

        print(mid)

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid)  
        elif arr[mid] < target:
            return binary_search(arr, target, mid, high)
        else:
            return -1
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

