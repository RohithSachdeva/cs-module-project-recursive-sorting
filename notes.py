"""
Random notes from Tuesday Lecture

Quicksort
-Divide and Conquer
-Split into subparts that are easier to work with
--No parallelism today 

[15, 32, 126, 4 ,7, 28, 96, 27, 52]
Unsorted array... 
1. Pick a pivot point .. Pick the first why not?  
2. Partition the rest of the elements around the pivot element. 
    -- First element = 15
    -- Two arrays around it... partition the higher elements to the right; lower to the left 
3.     [4, 7] [15] [32, 126, 28, 96, 27, 52]  

4. So then you can basically start pivoting the other arrays... where 32 is the pivot for that right array
    [4][7][15][][32][]           ... and so on.  eventually everything will sort itself out in separate arrays; faster than bubble and selection sort etc.

5.   Bubble and Selection Sort --> O(n^2)    Quicksort and Mergesort -> O(n*log n)   (log n sort of means you're cutting the work in half everytime / Breaking the array in half  )


Helper function to help partition the input array:
def partition(arr):
    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else: 
            right.append(x) 

        Now we have 3 arrays 
    return left, pivot, right

Now we want to recursively go through everything
def quicksort(arr):
    #base case
    #if the length of the array is less than or equal to 1.. no further sorting is needed
    if len(arr) <= 1:
        return arr
    
    #otherwise, we call the partition function to break it up.

    left 



"""

"""
MergeSort 
"""