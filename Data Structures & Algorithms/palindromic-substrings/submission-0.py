class Solution:
    def countSubstrings(self, s: str) -> int:
        self.length = len(s)
        max_len = 0
        max_l = 0
        max_r = 0
        total = 0
        for i in range(self.length):
            # odd length
            odd_count,l,r = self.helper(i,i,s)
            total+=odd_count
            # even length
            even_count,l,r = self.helper(i,i+1,s)
            total+=even_count
        return total
      
    def helper(self,l,r,word):
        max_len = 0
        max_l = 0
        max_r = 0
        count=0
        while l>=0 and r<self.length and word[l]==word[r]:
            count+=1
            max_l = l
            max_r = r
            l-=1
            r+=1
        return count,max_l,max_r



        