class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        count = {}

        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        for k in count:
            if count[k] == 2:
                result.append(k)

        return result
        