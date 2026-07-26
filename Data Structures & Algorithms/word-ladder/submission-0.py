import string
from collections import deque
class Solution:
    def generateMatchingWords(self,word):
        res = []
        for i in range(len(word)):
            for ch in string.ascii_lowercase:
                new_word = word[:i]+ch+word[i+1:]
                if new_word in self.word_list_set:
                    res.append(new_word)
        return res
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append((beginWord,1))
        self.word_list_set = set(wordList)
        while queue:
            matching_word,seq = queue.popleft()
            if matching_word==endWord:
                return seq
            if matching_word in self.word_list_set:
                self.word_list_set.remove(matching_word)
            res = self.generateMatchingWords(matching_word)
            for word in res:
                queue.append((word,seq+1))
        return 0

            
