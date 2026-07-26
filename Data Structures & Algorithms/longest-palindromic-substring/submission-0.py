class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.length = len(s)
        max_len = 0
        max_l = 0
        max_r = 0
        for i in range(self.length):
            # odd length
            str_len,l,r = self.helper(i,i,s)
            if(str_len>max_len):
                max_len = str_len 
                max_l = l
                max_r =r
            

            # even length
            str_len,l,r = self.helper(i,i+1,s)
            if(str_len>max_len):
                max_len = str_len 
                max_l = l
                max_r =r
        return s[max_l:max_r+1]
    def helper(self,l,r,word):
        max_len = 0
        max_l = 0
        max_r = 0
        while l>=0 and r<self.length and word[l]==word[r]:
            max_len = max(max_len,r-l+1)
            max_l = l
            max_r = r
            l-=1
            r+=1
        return max_len,max_l,max_r



        