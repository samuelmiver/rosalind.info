#!/usr/bin/python3

import re
import sys

def longest_common_substring(strings):
    '''Given a list of strings, return the longest common substring'''
    string = strings[0]
    # for every possible length (downwards):
    for length in range(len(string), 0, -1):
        # for every substring of that length
        for offset in range(0, len(string) + 1 - length):
            substr = string[offset: offset + length - 1]
            common = True
            for check_str in strings[1:]:
                if substr not in check_str:
                    common = False
                    break
            if common:
                return substr
    return None



if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "files/rosalind_lcsm.txt"
    with open(filename) as stream:
        seqs = re.findall(r'>\w+([ACGT\s]+)', stream.read())
        seqs = [seq.replace('\n', '') for seq in seqs]
        print(longest_common_substring(seqs))
