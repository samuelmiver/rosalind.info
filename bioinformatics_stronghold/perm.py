from itertools import permutations

def perm(n):
    perms = list(permutations(range(1,n+1)))
    return str(len(perms)) + '\n' + \
           '\n'.join([' '.join(map(str, p)) for p in perms])

if __name__ == '__main__':

    with open('files/rosalind_perm.txt','r') as fi:
        for line in fi:
            n = line.strip()

    print(perm(int(n)))
