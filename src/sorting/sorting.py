# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    m, a, b = 0, 0, 0
    while len(arrA) > a and len(arrB) > b:
        if arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
        elif arrA[a] > arrB[b]:
            merged_arr[m] = arrB[b]
            b += 1
        m += 1
    while len(arrA) > a:
        merged_arr[m] = arrA[a]
        m += 1
        a += 1
    while len(arrB) > b:
        merged_arr[m] = arrB[b]
        m += 1
        b += 1

    # for i in range(elements):
    #     if len(arrA) > 0 and len(arrB) > 0:
    #         if arrA[0] < arrB[0]:
    #             merged_arr.append(arrA.pop(0))
    #         elif arrA[0] > arrB[0]:
    #             merged_arr.append(arrB.pop(0))
    #     elif len(arrA) > 0 and len(arrB) == 0:
    #         merged_arr.append(arrA.pop(0))
    #     elif len(arrA) == 0 and len(arrB) > 0:
    #         merged_arr.append(arrB.pop(0))
    #     print(merged_arr)
            
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    mid =  len(arr) // 2
    lt_arr = arr[:mid]
    rt_arr = arr[mid:]

    if len(lt_arr) > 1:
        lt_arr = merge_sort(lt_arr)
    if len(rt_arr) > 1:
        rt_arr = merge_sort(rt_arr)

    return merge(lt_arr, rt_arr)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

