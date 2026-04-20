class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            num = nums[i]
            to_find = target - num
            if to_find in hash:
                return [hash[to_find], i]
            else:
                hash[num] = i           