from collections import defaultdict
from collections import Counter
class Solution(object):
        def containsDuplicate(self, nums):
            hash=Counter(nums)
            for value in hash.values():
                if value>1:
                    return True
                
            return False

    