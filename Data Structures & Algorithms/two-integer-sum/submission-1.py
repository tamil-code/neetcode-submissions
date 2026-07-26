class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache ={}
        for idx,val in enumerate(nums):
            temp = target-val
            if temp not in cache:
                cache[val] = idx
            else:
                return [cache[temp],idx]
        return [-1,-1]

            