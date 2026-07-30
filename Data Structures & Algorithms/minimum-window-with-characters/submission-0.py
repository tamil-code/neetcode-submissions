from collections import defaultdict,Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen=len(s)
        tlen = len(t)
        if tlen>slen:
            return ""
        need=Counter(t)
        have =defaultdict(int)
        required=len(need)
        formed=0
        l=0
        min_window=float('inf')
        res=[-1,-1]
        for r in range(len(s)):
            char=s[r]
            have[char]+=1
            if char in need and have[char]==need[char]: # met a required freq for a char
                formed+=1
            while formed==required:
                curr_window = (r-l)+1
                if curr_window<min_window:
                    min_window = curr_window
                    res=[l,r]
               # Remove left character
                left = s[l]
                have[left] -= 1

                # Window became invalid
                if left in need and have[left] < need[left]:
                    formed -= 1

                l += 1
        l,r=res
        return "" if min_window==float('inf') else s[l:r+1]



        