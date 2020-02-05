import importlib

problem_no = 'P218'  # Fill problem number here

if __name__ == '__main__':
    p = importlib.import_module(problem_no)
    if not hasattr(p, 'SI') or not hasattr(p, 'SO'):
        raise ValueError('Need sample input(SI) or sample output(SO)!')

    si, so = p.SI, p.SO
    if len(si) != len(so):
        raise ValueError('Number of sample input must equals to the number of sample output!')

    if not hasattr(p, 'Solution') or not hasattr(p, 'TM') or not hasattr(p.Solution, p.TM):
        raise ValueError('Need valid solution!')

    test_method = p.TM
    s = p.Solution()
    for i in range(len(si)):
        m = getattr(s, test_method)
        r = m(*si[i])
        if r != so[i]:
            print('Test case {} failed'.format(i))
        else:
            print('Test case {} passed'.format(i))
