def linear_search(arr, target):
    """
    Returns true if target is in arr, else false
    """
    # Loop through the array
    for i in range(len(arr)):
        # compare values
        if arr[i] == target:
            return i
        # else: keep looping
    # Finish looping:
    # We didn't find it. return False
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    """
    Returns true if target is in arr, else false
    """
    # remember to check the empty case
    # start = the starting index of the subset of the array we're searching in. inclusive
    # end = the end index of the subset -- inclusive
    start = 0
    end = len(arr) - 1
    while start <= end:
        # Look at the middle
        # how do we get the midpoint?
        # for the whole array, it's len(arr) / 2 - 1
        # for a subset of the array: (start + end) // 2
        middle_index = (start + end) // 2

        # Compare it to the target
        if arr[middle_index] > target:
            # search the right side
            # set start = middle_index + 1
            end = middle_index - 1
        elif arr[middle_index] < target:
            # search the left side: set end = middle_index - 1
            start = middle_index + 1
        else:
            return middle_index
        # Repeat
    # If not found, return False
    return -1
    # How do we know if it's not found?
        # the subset that we're looking at has 0 or negative length
    # How to represent the subset / "window" that we're searching in?
        # store start and end index in variables
        # start index + length of the subarray
        # pass around slices of the array - creates a new array, would use extra memory and time. you also lose the original indices
