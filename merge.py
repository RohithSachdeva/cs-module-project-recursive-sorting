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
            a += 1

    if b == len(arrB):
        for item in arrA[a:]:
            merged_arr[merged_index] = arrA[a]
            merged_index += 1
            b += 1
    


    # Your code here
    #We have to keep track of multiple indices 





    return merged_arr

print(merge([3, 6], [4, 9]))