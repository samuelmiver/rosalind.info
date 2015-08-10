#!/usr/bin/env python

def bins():

    with open('./files/rosalind_bins.txt', 'r') as f:
        lines = []
        for line in f:
            line = line.strip().split()
            new_line = line

            lines += [new_line,]

    # Process the content
    n = int(lines[0][0])
    fix_m = int(lines[1][0])

    array = [int(x) for x in lines[2]]
    integers = [int(x) for x in lines[3]]

    # There is better ways to do the apporach, but the idea is to use the divide and conquer algorithm

    results = []
    for integer in integers:
        flag = None
        m = fix_m//2
        half_list_value = array[m]

        if integer == half_list_value:
            results.append(m+1)
            flag = True

        elif integer < half_list_value:
            while m >= 0:
                if integer == array[m]:
                    results.append(m+1)
                    flag = True
                    break
                m-=1
        else:
            while m < len(array):
                if integer == array[m]:
                    results.append(m+1)
                    flag = True
                    break
                m+=1

        if not flag:
            results.append(-1)
        else:
            pass

    # print the results:
    final = []
    for result in results:
        if -1 <= result <= n:
            final.append(str(result))

    print(' '.join(final))

if __name__ == "__main__":
    bins()
