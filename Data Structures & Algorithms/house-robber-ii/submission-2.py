class Solution:
    def robber(self,nums:List[int])->int:
        # each step has two choices
        # 1. skip the house dp[i] = dp[i-1] keep the prev amt
        # 2. rob the house dp[i] = nums[i] + dp[i-2] (current money + best money until before the prev house)
        n = len(nums)
        if n==1:
            return nums[0]
        prev1 = nums[0]
        prev2 = max(nums[0],nums[1])
        curr = 0
        for i in range(2,n):
            curr = max(prev2,nums[i]+prev1)
            prev1,prev2 = prev2,curr
        return prev2
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        robbery1 = self.robber(nums[0:n-1]) # skipping the last house
        robbery2 = self.robber(nums[1:n]) # skipping the first house
        return max(robbery1,robbery2)