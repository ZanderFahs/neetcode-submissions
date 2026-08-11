class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        imap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in imap:
                return [imap[complement], i]
            imap[num] = i