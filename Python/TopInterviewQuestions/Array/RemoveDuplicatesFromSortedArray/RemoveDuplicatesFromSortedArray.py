class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        orig = 0
        srav = 0
        while srav < len(nums):
            if nums[orig] == nums[srav]:
                srav +=1
            else:
                orig +=1
                nums[orig] = nums[srav]
        return orig + 1