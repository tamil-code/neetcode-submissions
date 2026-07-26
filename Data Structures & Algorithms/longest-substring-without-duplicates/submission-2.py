class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache={}
        left,right = 0,0
        result = 0
        while (right < len(s)):
            if s[right] not in cache:
                cache[s[right]] = 1
                right += 1
            else:
                cache[s[left]] = cache[s[left]] - 1
                if (cache[s[left]] == 0):
                    del cache[s[left]]
                left += 1
            result = max(result, right - left)
        return result


