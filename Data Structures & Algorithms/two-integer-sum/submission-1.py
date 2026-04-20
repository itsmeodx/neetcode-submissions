class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = j = 0
        for num1 in nums:
            for num2 in nums:
                if num1 + num2 == target and i != j:
                    return [i, j]
                j += 1
            i += 1
            j = 0