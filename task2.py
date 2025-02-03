class LongestCommonWord:
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        prefix = strings[0]

        for word in strings[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix


if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["prefix", "preface", "preform"]
    assert trie.find_longest_common_word(strings) == "pre"

    print("All tests passed!")
