def freq_word(filename):
    """Given a string with repetitive motifs, the functions finds
    the most frequent k-mers with length of that integer.

    """
    with open(filename) as filehandle:
        seq = filehandle.readline().strip()
        k = int(filehandle.readline())

    dictionary = {}
    for i in range(len(seq) - k + 1):
        if seq[i:i + k] in dictionary:
            dictionary[seq[i:i + k]] += 1
        else:
            dictionary[seq[i:i + k]] = 0

    max_value = max(dictionary.values())
    results_list = []

    for subseq, repetition in dictionary.items():
        if repetition == max_value:
            results_list.append(subseq)

    return results_list

# Execution part:

x = freq_word("./files/rosalind_1a.txt")

print ('%s' % ' '.join(map(str, x)))