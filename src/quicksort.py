# helper function to partition the input array 
def partition(arr):
    # pick a pivot 
    pivot = arr[0]
    left = []
    right = []
    
    # partition the elements around the pivot 
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    # we have elements partitioned in the left, pivot, and right arrays 
    return left, pivot, right 

def quicksort(arr):
    # base case if len array <= 1 
    if len(arr) <= 1:
        return arr

    # otherwise, we need to call our partition function to break the inpu
    # array into smaller chunks 
    left, pivot, right = partition(arr)
    
    # stick the pivot in a list 
    pivot = [pivot]

    # run quicksort on left and right chunks 
    # to break them down further into smaller pieces 
    qleft = quicksort(left)
    qright = quicksort(right)

    # concatenate all the pieces together 
    return qleft + pivot + qright
        

arr = [13, 17, 5, 18, 27, 22, 16, 3]
arr = quicksort(arr)
print(arr)
