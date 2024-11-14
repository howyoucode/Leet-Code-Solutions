# Remove Duplicates from Sorted Array

This is a Python implementation of the "Remove Duplicates from Sorted Array" problem. Given an integer array `nums` sorted in non-decreasing order, the task is to remove duplicates in-place such that each unique element appears only once. The relative order of the elements should remain the same.

## Problem Description

- **Input:** A sorted array `nums[]`.
- **Output:** An integer `k`, which is the number of unique elements in `nums[]`, such that the first `k` elements of `nums[]` contain the unique elements in the order they were present initially. The remaining elements in the array are not important and can be ignored.

### Example

```python
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
run = Solution()
length = run.removeDuplicates(nums)

print(nums[:length])
