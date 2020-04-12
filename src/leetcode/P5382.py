C = {
    '&quot;': '"',
    '&apos;': '\'',
    '&amp;': '&',
    '&gt;': '>',
    '&lt;': '<',
    '&frasl;': '/',
}


class Solution:
    def entityParser(self, text: str) -> str:
        for k, v in C.items():
            text = text.replace(k, v)
        return text


if __name__ == '__main__':
    print(Solution().entityParser(text="&apos;Stay home! Practice on Leetcode :)&apos;"))
