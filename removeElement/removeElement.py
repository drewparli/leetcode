__author__    = "Andrew Parli"
__copyright__ = "Copyright 2018, Andrew Parli"

def removeElement(nums, val):
    """
    Removes all occurences of `val` from `nums`.
        :type nums: List[int]
        :type val: int
        :rtype: int
    """
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums.pop(i)
            n -= 1
        else:
            i += 1
    return i

if __name__ == '__main__':

    # Example 1
    nums = [3,2,2,3]
    val = 3
    expectedLength = 2
    expectedNums = [2,2]
    result = removeElement(nums, val)
    assert(result == expectedLength)
    assert(nums == expectedNums)

    # Example 2
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    expectedLength = 5
    expectedNums = [0,1,3,0,4]
    result = removeElement(nums, val)
    assert(result == expectedLength)
    assert(nums == expectedNums)

    # Edge case 1 - empty list
    nums = []
    val = -100
    expectedLength = 0
    expectedNums = []
    result = removeElement(nums, val)
    assert(result == expectedLength)
    assert(nums == expectedNums)

    # Edge case 2 - array full of val
    nums = [3,3,3,3,3,3,3,3,3,3]
    val = 3
    expectedLength = 0
    expectedNums = []
    result = removeElement(nums, val)
    assert(result == expectedLength)
    assert(nums == expectedNums)
