class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # Pointer for the position of the next unique element
        unique_pos = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_pos]:
                unique_pos += 1
                nums[unique_pos] = nums[i]
        
        return unique_pos + 1

nums = [0,0,1,1,1,2,2,3,3,4]
run = Solution()
length = run.removeDuplicates(nums)

# Printing the unique elements
print(nums[:length])
