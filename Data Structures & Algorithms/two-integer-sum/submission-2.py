class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for num1 in nums:
            j = i + 1
            for num2 in nums[j:]:
                if num1 + num2 == target:
                    return [i, j]
                j += 1
            i += 1