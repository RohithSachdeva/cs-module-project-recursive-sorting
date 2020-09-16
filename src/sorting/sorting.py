# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0
    b = 0
    merged_index = 0

    while a < len(arrA) and b < len(arrB):

        if arrA[a] > arrB[b]:
            merged_arr[merged_index] = arrB[b]
            merged_index += 1
            b += 1
        else:
            merged_arr[merged_index] = arrA[a]
            merged_index += 1
            a += 1
    #Check if arrA is empty, if it is dump values of arrB into sorted array

    if a == len(arrA):
        for item in arrB[b:]:
            merged_arr[merged_index] = arrB[b]
            merged_index += 1
            b += 1

    if b == len(arrB):
        for item in arrA[a:]:
            merged_arr[merged_index] = arrA[a]
            merged_index += 1
            a += 1
    

    return merged_arr

print(merge([1,8], [2,22]))



# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #Set base case ... in case the array is 1 elemenet.
    #Want to split the single array into 2 arrays and then can call the helper function 
    if len(arr) > 1:
        middle = len(arr) // 2
        left_array = arr[:middle]
        left_side = merge_sort(left_array)
        right_array = arr[middle:]
        right_side = merge_sort(right_array)
        merged_array = merge(left_side, right_side)
        return merged_array
    else:
        return arr





"""
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
"""




