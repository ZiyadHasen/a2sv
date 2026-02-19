class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
              value_at_i = nums[i]
              target_value = nums[value_at_i]
              ans.append(target_value)
        return ans
        