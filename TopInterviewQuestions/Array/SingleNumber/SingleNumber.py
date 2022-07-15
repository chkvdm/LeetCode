# version_1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value = dict()
        for num in nums:
            value[num] = value.get(num, 0) + 1
        for key, val in value.items():
            if val == 1:
                return key


# version_2

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value = Counter(nums)
        for key, val in value.items():
            if val == 1:
                return key