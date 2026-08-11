from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sortnums = sorted(nums, key = lambda x: (-freq[x],x))
        output = []
        for i in range(k):
            output.append(sortnums[0])
            sortnums = [x for x in sortnums if x != sortnums[0]]
        return output