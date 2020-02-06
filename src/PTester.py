class PTester(object):
    def __init__(self, si, so, cls, tm):
        if len(si) != len(so):
            raise ValueError('Number of sample input must equals to the number of sample output!')

        if not hasattr(cls, tm):
            raise ValueError('Need valid solution!')

        self.si, self.so, self.cls, self.tm = si, so, cls, tm

    def run(self):
        si, so = self.si, self.so
        s = self.cls()
        tm = self.tm
        for i in range(len(si)):
            m = getattr(s, tm)
            r = m(*si[i])
            if r != so[i]:
                print('Test case {} failed'.format(i))
            else:
                print('Test case {} passed'.format(i))
