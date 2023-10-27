from abc import abstractmethod, ABC
from collections import defaultdict
from typing import List, Protocol


class GroupingStrategy(Protocol):
    @abstractmethod
    def solve(self, strs: List[str]) -> List[List[str]]:
        pass


class NaiveGroupingStrategy(GroupingStrategy, ABC):
    def __init__(self):
        self.memoized_anagrams = {}

    def solve(self, strs):
        groups = []
        words_added = set()
        while strs:
            word = strs[0]
            strs = strs[1:]
            if word not in words_added:
                anagrams = self.get_all_anagrams(word, strs)
                words_added.update(anagrams)
                words_added.add(word)
                anagrams.append(word)
                groups.append(anagrams)
        return groups

    def get_all_anagrams(self, word, strs):
        anagrams = []

        for other_word in strs:
            if other_word not in self.memoized_anagrams and self.is_anagram(word, other_word):
                anagrams.append(other_word)

        return anagrams

    def is_anagram(self, word, other_word):
        if len(word) != len(other_word):
            return False

        if (word, other_word) in self.memoized_anagrams or (other_word, word) in self.memoized_anagrams:
            return True

        total_counts = defaultdict(int)

        for char in word:
            total_counts[char] += 1

        for char in other_word:
            total_counts[char] -= 1

        result = all(value == 0 for value in total_counts.values())

        if result:
            # Memoize the anagram pair.
            self.memoized_anagrams[(word, other_word)] = True

        return result


class SortedGroupingStrategy(GroupingStrategy, ABC):
    def solve(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_groups[sorted_word].append(word)

        return list(anagram_groups.values())

class Solution:
    def __init__(self, strategy=SortedGroupingStrategy):
        self.strategy = strategy()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.strategy.solve(strs)
