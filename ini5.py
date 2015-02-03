# to load a file in array format

with open("file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)


#in order to extract the even lines:

#First add a empty line at the beginning

array[::2]