class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while start<=end:
            mid = (start+end)//2
            if self.valid(mid,piles,h):
                end=mid-1
            else:
                start=mid+1
        return start

    def valid(self,rate_k,piles,hour)->bool:
        calc_hour = 0
        for pile in piles:
            if rate_k>pile:
                calc_hour+=1
            else:
                calc_hour+=math.ceil(pile/rate_k)
        return calc_hour<=hour