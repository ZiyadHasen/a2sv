class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        stack=[]
        index=0
        
        for i in range (n):
          if nums[i] in stack:
            continue
          else:
            stack.append(nums[i])
            nums[index]=nums[i]
            index+=1
        return index

       
        