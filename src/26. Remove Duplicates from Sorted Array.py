"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
"""


def removeDuplicates(nums):
    l, r = 0, 1
    while r < len(nums):
        if nums[l] == nums[r]:
            r += 1
        else:
            l += 1
            nums[l] = nums[r]
    return l + 1


if __name__ == "__main__":
    print(removeDuplicates([1, 1, 2]))
