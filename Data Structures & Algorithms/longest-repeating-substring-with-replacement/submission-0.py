from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  
       l,r=0,0
       char_freq = defaultdict(int)
       max_freq = 0
       res = 0
       while r<len(s):
         char_freq[s[r]]+=1
         max_freq = max(char_freq[s[r]],max_freq)
         curr_window_len = r-l+1
         is_valid_window = (curr_window_len - max_freq) <=k
         while not is_valid_window:
            char_freq[s[l]]-=1
            l+=1
            curr_window_len = r-l+1
            is_valid_window = (curr_window_len - max_freq) <=k
         res = max(res,curr_window_len)
         r+=1
       return res
        

