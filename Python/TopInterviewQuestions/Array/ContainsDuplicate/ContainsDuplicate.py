# version1

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for n in range(len(nums)-1):
            if (nums[n+1] - nums[n]) == 0:
                return True


# version2

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True