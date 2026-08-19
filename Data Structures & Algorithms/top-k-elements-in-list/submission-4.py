class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #convert nums to a hashmap
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        #create heap
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k: #if the heap gets to over size k, we remove the smallest thing in the queue. or in this case we pop it
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res