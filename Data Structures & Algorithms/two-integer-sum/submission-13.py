class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in hash:
                return [hash[to_find], i]
            else:
                hash[num] = i           