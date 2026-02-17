from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        max_val = max(right, max(end for _, end in ranges))
        covered = [False] * (max_val + 1)

        for start, end in ranges:
            for x in range(start, end + 1):
                covered[x] = True

        for x in range(left, right + 1):
            if not covered[x]:
                return False

        return True