from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str) or not pattern:
            raise ValueError("The pattern must be a non-empty string.")

        count = 0
        
        def _count_suffix(node, suffix):
            nonlocal count
            
            if node.is_end_of_word and suffix == "":
                count += 1
            
            for char, child in node.children.items():
                if suffix and suffix[0] == char:
                    _count_suffix(child, suffix[1:])
                else:
                    _count_suffix(child, suffix)
            
        _count_suffix(self.root, pattern)
        return count

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str) or not prefix:
            raise ValueError("The prefix must be a non-empty string.")

        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    
    for i, word in enumerate(words):
        trie.put(word, i)
    
    assert trie.count_words_with_suffix("e") == 1  # "apple"
    assert trie.count_words_with_suffix("ion") == 1  # "application"
    assert trie.count_words_with_suffix("a") == 1  # "banana"
    assert trie.count_words_with_suffix("at") == 1  # "cat"

    assert trie.has_prefix("app") == True  # "apple", "application"
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # "banana"
    assert trie.has_prefix("ca") == True  # "cat"
