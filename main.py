from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        words_added = {}
        while strs:
            word = strs[0]
            if word not in words_added:
                strs.remove(word)
                words = self.get_all_anagrams(word, strs)
                groups.append(words)
                for word_to_add in words:
                    if word_to_add != word and len(strs) > 0:
                        strs.remove(word_to_add)
                    words_added[word_to_add] = True

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