class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1 = {}
        hash_2 ={}
        for i in s:
            hash_1[i] = hash_1.get(i,0)+1
        for i in t:
            hash_2[i] = hash_2.get(i,0)+1
    
        return hash_1==hash_2
