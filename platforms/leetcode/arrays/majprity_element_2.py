class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        for x in nums:
            s = str(x)             
            if s not in freq:
                freq[s] = 0
            freq[s] += 1

        res = []
        for s, count in freq.items():
            if count > n // 3:
                res.append(int(s))  
        return res       