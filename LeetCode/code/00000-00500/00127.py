from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)
        q = deque()
        q.append(beginWord)
        visited = set(beginWord)
        word_len = len(beginWord)
        step = 1
        while q:
            cur_size = len(q)
            for i in range(cur_size):
                word = q.popleft()
                word_list = list(word)
                for j in range(word_len):
                    orgin_char = word_list[j]
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                visited.add(next_word)
                                q.append(next_word)
                    word_list[j] = orgin_char
            step += 1
        return 0
