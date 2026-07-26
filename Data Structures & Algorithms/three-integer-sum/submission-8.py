class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        k=0
        for i in range(len(nums)-2):
            # skip duplicate nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total==k:
                    res.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif total<k:
                    left+=1
                else:
                    right-=1
        return [list(t) for t in res]
