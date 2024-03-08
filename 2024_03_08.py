# Given an array of numbers arr and a window of size k, print out the median of each window of size k starting from the left and moving right by one position each time.
#
# For example, given the following array and k = 3:
# [-1, 5, 13, 8, 2, 3, 3, 1]
# Your function should print out the following:
#
# 5 <- median of [-1, 5, 13]
# 8 <- median of [5, 13, 8]
# 8 <- median of [13, 8, 2]
# 3 <- median of [8, 2, 3]
# 3 <- median of [2, 3, 3]
# 3 <- median of [3, 3, 1]
# Recall that the median of an even-sized list is the average of the two middle numbers.


def median(arr: list) -> int:
    arr.sort()
    no_of_elements: int = len(arr)

    if no_of_elements % 2 == 0:
        mid_left = arr[(no_of_elements // 2) - 1]
        mid_right = arr[no_of_elements // 2]
        return (mid_left + mid_right) / 2

    return arr[no_of_elements // 2]


def slice_and_median(arr: list, window: int) -> None:
    for i in range(0, len(arr)):
        if (i + window) > len(arr):
            break

        print(median(arr[i:i+window]), "<- median of ", arr[i:i+window])


slice_and_median([-1, 5, 13, 8, 2, 3, 3, 1], 3)
