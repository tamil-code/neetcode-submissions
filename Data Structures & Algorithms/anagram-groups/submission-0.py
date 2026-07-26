class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for i in range(len(strs)):
            char_arr = [0 for i in range(0,26)]
            for char in strs[i]:
                char_int = ord(char) - ord('a')
                char_arr[char_int]+=1
            group_anagrams[tuple(char_arr)].append(i)
        result_arr=[]
        for vals in group_anagrams.values():
            temp_arr = [word for i,word in enumerate(strs) if i in vals]
            result_arr.append(temp_arr)
        return result_arr