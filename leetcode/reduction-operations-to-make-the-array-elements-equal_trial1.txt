from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        steps = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                steps += 1
            res += steps

        return res
