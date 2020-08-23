from data_structure.trie import Trie


class StreamChecker:

    def __init__(self, words):
        t = Trie()
        for word in words:
            rw = ''.join(list(reversed(word)))
            t.insert(rw, True)
        self.t = t
        self.q = []

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        r = self.t.root
        for i in reversed(self.q):
            if i not in r.next:
                return False
            r = r.next[i]
            if r.val is not None:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
if __name__ == '__main__':
    o = StreamChecker(["cd", "f", "kl"])
    for i in range(15):
        print(o.query(chr(i + 97)))
