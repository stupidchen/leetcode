def depth(path):
    r = 0
    while r < len(path) and path[r] == '\t':
        r += 1
    return r


def is_file(path):
    return '.' in path


class Solution:
    def lengthLongestPath(self, input):
        s = ['']
        d = [-1]
        r = 0
        for path in input.split('\n'):
            td = depth(path)
            while td <= d[-1]:
                s.pop()
                d.pop()
            s.append(path.replace('\t', ''))
            d.append(td)

            if is_file(path):
                t = '/'.join(s)
                l = len(t) - 1
                if l > r:
                    r = l
        return r


# For test only
SI = (('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',),)
SO = (len('dir/subdir2/subsubdir2/file2.ext'),)
TM = 'lengthLongestPath'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
