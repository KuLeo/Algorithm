from collections import defaultdict


class TrieF:

    def __init__(self):
        self.__final = False
        self.__nodes = {}

    def __repr__(self):
        return 'Trie<len={}, final={}>'.format(len(self), self.__final)

    def __getstate__(self):
        return self.__final, self.__nodes

    def __setstate__(self, state):
        self.__final, self.__nodes = state

    def __len__(self):
        return len(self.__nodes)

    def __bool__(self):
        return self.__final

    def __contains__(self, array):
        try:
            return self[array]
        except KeyError:
            return False

    def __iter__(self):
        yield self
        for node in self.__nodes.values():
            yield from node

    def __getitem__(self, array):
        return self.__get(array, False)

    def create(self, array):
        self.__get(array, True).__final = True

    def read(self):
        yield from self.__read([])

    def update(self, array):
        self[array].__final = True

    def delete(self, array):
        self[array].__final = False

    def prune(self):
        for key, value in tuple(self.__nodes.items()):
            if not value.prune():
                del self.__nodes[key]
        if not len(self):
            self.delete([])
        return self

    def __get(self, array, create):
        if array:
            head, *tail = array
            if create and head not in self.__nodes:
                self.__nodes[head] = Trie()
            return self.__nodes[head].__get(tail, create)
        return self

    def __read(self, name):
        if self.__final:
            yield name
        for key, value in self.__nodes.items():
            yield from value.__read(name + [key])


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("test")
    if trie.search("test"):
        print("Exist")
    if not trie.search("apple"):
        print("Not exist")
    if trie.starts_with("te"):
        print("Exist")
