class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            group_anagrams[key].append(word)
        return  list(group_anagrams.values())