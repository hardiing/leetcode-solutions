class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 # start by pointing at second node since first is unique

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]: # if pointer value is not equal to the value to its left
                nums[l] = nums[r] # set pointer to that value
                l += 1 # increment to next spot in array

        return l