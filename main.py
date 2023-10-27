from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        words_added = {}
        for word in strs:
            if word not in words_added:
                excluded_word = strs.copy()
                excluded_word.remove(word)
                words = self.get_all_anagrams(word, excluded_word)
                groups.append(words)
                for word in words:
                    words_added[word] = True

        return groups


    def get_all_anagrams(self, word, strs):
        anagrams = []
        for other_word in strs:
            if self.is_anagram(word, other_word):
                anagrams.append(other_word)

        anagrams.append(word)
        return anagrams

    def is_anagram(self, word, other_word):
        if len(word) != len(other_word):
            return False

        total_counts = defaultdict(int)

        for char in word:
            total_counts[char] += 1

        for char in other_word:
            total_counts[char] -= 1

        return all(value == 0 for value in total_counts.values())