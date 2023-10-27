from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.memoized_anagrams = {}

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        words_added = {}
        while strs:
            word = strs[0]
            strs.remove(word)
            if word not in words_added:
                words = self.get_all_anagrams(word, strs)
                for word_to_add in words:
                    if len(strs) > 0:
                        strs.remove(word_to_add)

                    words_added[word_to_add] = True

                words_added[word] = True
                words.append(word)
                groups.append(words)

        return groups


    def get_all_anagrams(self, word, strs):
        anagrams = []
        for other_word in strs:
            if self.is_anagram(word, other_word):
                anagrams.append(other_word)

        return anagrams

    def is_anagram(self, word, other_word):
        if len(word) != len(other_word):
            return False
        
        if other_word in self.memoized_anagrams:
            return True

        total_counts = defaultdict(int)

        for char in word:
            total_counts[char] += 1

        for char in other_word:
            total_counts[char] -= 1

        result = all(value == 0 for value in total_counts.values())
        if result:
            self.memoized_anagrams[other_word] = result

        return result
