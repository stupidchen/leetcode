from collections import Counter

MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.",
         "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


class Solution:
    def uniqueMorseRepresentations(self, words):
        def get_morse(word):
            r = ''
            for c in word:
                r += MORSE[ord(c) - 97]
            return r

        return len(Counter([get_morse(word) for word in words]).keys())
