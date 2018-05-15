"""
PROBLEM STATEMENT
=================
Given a sorted array `nums`, remove the duplicates in-place such that
each element appears only once and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

THE SOLUTION
============
Not only can we solve this task with O(1) extra memory, we can also
solve it in linear time, 0(n).

Trivial cases include:
    len(nums) -> 0    -- an empty list
    len(nums) -> 1    -- list with a single element

Memory needs to be allocated for the following:
    init_size : the initial length of `nums`
    remaining : init_size less the current number of elements
                removed from `nums`
    i : index of current element in `nums`
    j : index of next element in `nums`

Looking at the elements of `nums` indexed by `i` and `j`, if these
elements are equal, then the value indexed by `j` is removed from
`nums` and `remaining` is decremented by `1`. Otherwise, both `i` and
`j` are incremented by `1`. If `j` is less than `remaining` then
repeat, otherwise return the value of `remaining`.

EXAMPLE
=======
    init_size = 8
    remaining = 8
          i j
          0 1 2 3 4 5 6 7
    nums [1,1,2,2,3,4,4,5]
    -----------------------------------------------------------------
    nums[i] == nums[j] -> remove(nums, j), decrement(remaining, 1)

    init_size = 8
    remaining = 1
          i j
          0 1 2 3 4 5 6
    nums [1,2,2,3,4,4,5]
    -----------------------------------------------------------------
    nums[i] != nums[j] -> increment(i, 1), increment(j, 1)

    init_size = 8
    remaining = 1
            i j
          0 1 2 3 4 5 6
    nums [1,2,2,3,4,4,5]
    -----------------------------------------------------------------
    nums[i] == nums[j] -> remove(nums, j), decrement(remaining, 1)

    init_size = 8
    remaining = 2
            i j
          0 1 2 3 4 5
    nums [1,2,3,4,4,5]
    -----------------------------------------------------------------
    nums[i] != nums[j] -> decrement(i, 1), decrement(j, 1)

    init_size = 8
    remaining = 2
              i j
          0 1 2 3 4 5
    nums [1,2,3,4,4,5]
    -----------------------------------------------------------------
    nums[i] != nums[j] -> decrement(i, 1), decrement(j, 1)

    init_size = 8
    remaining = 2
                i j
          0 1 2 3 4 5
    nums [1,2,3,4,4,5]
    -----------------------------------------------------------------
    nums[i] == nums[j] -> remove(nums, j), decrement(remaining, 1)

    init_size = 8
    remaining = 3
                i j
          0 1 2 3 4
    nums [1,2,3,4,5]
    -----------------------------------------------------------------
    nums[i] != nums[j] -> decrement(i, 1), decrement(j, 1)

    init_size = 8
    remaining = 3
                  i j
          0 1 2 3 4 5
    nums [1,2,3,4,5]
    -----------------------------------------------------------------
    j == remaining -> return remaining -> 5
"""
def removeDuplicates(nums):
    init_size = len(nums)

    if init_size < 2:
        return init_size

    remaining = init_size

    i,j = 0,1
    while j < remaining:
        if nums[j] == nums[i]:
            nums.pop(j)
            remaining -= 1
        else:
            i += 1
            j += 1

    return remaining

def applySolution(nums):
    expected_nums = list(set(nums))
    expected_nums.sort()
    expected_length = len(expected_nums)
    observered_length = removeDuplicates(nums)
    return expected_length, expected_nums, observered_length, nums

def assertCorrect(exp_length, exp_nums, obs_length, nums):
    assert(nums == exp_nums)
    assert(obs_length == exp_length)


if __name__ == '__main__':

    # test 0
    nums = []
    assertCorrect(*applySolution(nums))

    # test 1
    nums = [123]
    assertCorrect(*applySolution(nums))

    # test 2
    nums = [1,1,2,2,3,4,4,5]
    assertCorrect(*applySolution(nums))

    # test 3
    nums = [1,1,2,2,2,2,3,4,5,5,5,5,6,7,8,9,10,10,10,10,10]
    assertCorrect(*applySolution(nums))