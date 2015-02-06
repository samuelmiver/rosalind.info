data = [line.strip("\n") for line in open("./files/rosalind_1d.txt", "r")]

genome = data[0]
values = data[1].split()
k = int(values[0])
L = int(values[1])
t = int(values[2])


def makeCandidates(genome):
    candidates = []
    for i in range(0, len(genome)):
        candidate = genome[i: i + k]
        if candidate in candidates or len(candidate) < k:
            pass
        else:
            candidates.append(candidate)
    return candidates


def makeWindows(genome):
    windows = []
    for i in range(0, len(genome)):
        window = genome[i: i + L]
        if window in windows or len(window) < L:
            pass
        else:
            windows.append(window)
    return windows


def matches(candidate, window):
    count = 0
    for i in range(0, len(window)):
        if count >= t or len(window[i: i + k]) < k:
            break
        elif window[i: i + k] == candidate:
            count += 1
    return count


candidates = makeCandidates(genome)
windows = makeWindows(genome)

print (matches(candidates,windows))