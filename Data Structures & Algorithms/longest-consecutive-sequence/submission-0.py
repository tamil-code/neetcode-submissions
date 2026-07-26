class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            cache[num] = 1
        res = 0

        for num in nums:
            temp = 0
            val = num
            while(val in cache):
                temp += 1
                val += 1
            res = max(res, temp)

        return res;


        