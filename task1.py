from trie import Trie, TrieNode


class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Suffix pattern must be a string.")
        if pattern == "":
            return self.size

        def search(node: TrieNode, suffix, subsuffix = None) -> int:
            count = 0
            if subsuffix == "":
                subsuffix = None
                if node.value is not None:
                    count += 1
            for char, child_node in node.children.items():
                new_ssubsuffix = None
                if subsuffix is not None:
                    if char == subsuffix[0]: new_ssubsuffix = subsuffix[1:]
                elif char == suffix[0]:
                    new_ssubsuffix = suffix[1:]
                count += search(child_node, suffix, new_ssubsuffix)
            return count

        cnt = search(self.root, pattern)
        return cnt

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string.")

        current = self.root
        for char in prefix:
            if char not in current.children: return False
            current = current.children[char]

        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
