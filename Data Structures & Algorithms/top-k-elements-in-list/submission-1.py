class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache={}
        buckets = [[] for _ in range(len(nums)+1)]
        result = []
        for num in nums:
            cache[num] = cache.get(num,0)+1
        for num,freq in cache.items():
            buckets[freq].append(num)
        print("Buckets: ",buckets)
        for freq in range(len(nums),0,-1):
            print("freq: ",freq)
            for bucket in buckets[freq]:
                result.append(bucket)
            if len(result)==k:
                return result
        return result
