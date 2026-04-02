from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0: -1}
        s = 0

        for i, n in enumerate(nums):
            s += n
            r = s % k

            if r in rem:
                if i - rem[r] > 1:
                    return True
            else:
                rem[r] = i

        return False
