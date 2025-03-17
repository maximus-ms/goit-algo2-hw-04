from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, (list, tuple, set)) or len(strings) == 0:
            return ""
        for string in strings:
            if not isinstance(string, str):
                raise TypeError("input must be a list of strings")
            self.put(string)

        current = self.root
        longest_common_word = ""
        while current.children:
            if len(current.children) > 1:
                return longest_common_word
            key = list(current.children.keys())[0]
            longest_common_word += key
            current = current.children[key]
        return longest_common_word


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
