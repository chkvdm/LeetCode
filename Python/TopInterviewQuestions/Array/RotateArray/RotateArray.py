class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        for i in range(k):
            nums.append(nums[i])
        nums[:] = list(reversed(nums[k:]))