# 27. Remove Element

Given an array `nums` and a value `val`, remove all instances of that value
__in-place__ and return the new length.

Do not allocate extra space for another array, you must do this by __modifying
the input array in-place__ with *O(1)* extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

#### Example 1:

    nums = [3, 2, 2, 3]
    val = 3

Your function should return

    length = 2
    nums[0:2] = [2, 2]

It doesn't matter what you leave beyond the returned length.

#### Example 2:

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

Your function should return

    length = 5
    nums[0:5] = [0, 1, 3, 0, 4]

NOTE: The order of the first five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.