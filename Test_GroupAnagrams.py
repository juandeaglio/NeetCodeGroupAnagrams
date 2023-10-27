import unittest

from main import Solution


def compare_elements(expected, groups):
    for group in expected:
        for element in group:
            found = False
            for group2 in groups:
                if element in group2:
                    found = True

            if not found:
                return False

    return True


class Test_GroupAnagrams(unittest.TestCase):
    def test_group_some_anagrams(self):
        groups = Solution().groupAnagrams(["eat", "tea"])
        expected = [["eat","tea"]]
        self.assertTrue(compare_elements(expected, groups))


if __name__ == '__main__':
    unittest.main()
