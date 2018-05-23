#!/usr/bin/env python


def ilis(l):

    lis = [[e] for e in l]
    for i, e in enumerate(l):
        lower_tuples = filter(lambda (a,b): b<e, enumerate(l[:i]))
        if not lower_tuples: continue
        lowerlises = [lis[a] for a,b in  lower_tuples ]
        lis[i] = max(lowerlises, key=len) + [e]
    return max(lis, key=len)

def dlis(l):

    lis = [[e] for e in l]
    for i, e in enumerate(l):
        lower_tuples = filter(lambda (a,b): b>e, enumerate(l[:i]))
        if not lower_tuples: continue
        lowerlises = [lis[a] for a,b in  lower_tuples ]
        lis[i] = max(lowerlises, key=len) + [e]
    return max(lis, key=len)

def lgis(fil):

    with open(fil, 'rU') as fi:
        for line in fi:
            line = line.strip().split()


    line = [int(i) for i in line]
    print ' '.join([str(i) for i in ilis(line)])
    print ' '.join([str(i) for i in dlis(line)])





if __name__ == '__main__':
    lgis('./files/rosalind_lgis.txt')
