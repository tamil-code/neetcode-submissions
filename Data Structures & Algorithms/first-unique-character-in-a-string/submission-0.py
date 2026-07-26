class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map.get(i,0)+1
        for idx,i in enumerate(s):
            if hash_map[i]==1:
                return idx
        return -1