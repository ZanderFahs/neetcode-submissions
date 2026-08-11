class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lmap = {}
   
        for i, num in enumerate(nums):
            j = target - num
            if j in lmap:
                return [lmap[j], i]
            lmap[num] = i
        return []