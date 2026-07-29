from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)
        for ch in s1:
            freq_s1[ch]+=1
        l,r=0,0
        while r<len(s2):
            freq_s2[s2[r]]+=1
            curr_window = r-l+1
            if curr_window > len(s1):
                freq_s2[s2[l]]-=1
                if freq_s2[s2[l]]==0:
                    del freq_s2[s2[l]]
                l+=1
                curr_window = r-l+1

            if curr_window==len(s1) and freq_s1 == freq_s2:
                return True

            r+=1
        return False
            
            


