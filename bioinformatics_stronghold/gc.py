def GC_counter (multifasta_file):
    
    """From a multifasta file, computes the GC content (in 100%) of each one and retrieves
    the identifier and the content of that one with the greatest value"""

    #Create two lists with identifiers and sequences

    nameslist = []
    seqslist = []
    data = ''

    fd = open (multifasta_file)
    for line in fd:
        if line[0] == ">":
            nameslist.append(line[1:].strip())
            if data != '':
                seqslist.append(data)
            data=''
        else:
            data += line.strip()
    seqslist.append(data)

    #GC counter
    cCount = 0
    gCount = 0
    gcCount = 0
    GCContent = .0
    tmpGCContent = .0
    identifiers = ''
    x = 0

    for seq in seqslist:
        gCount = seq.count("G")
        cCount = seq.count("C")
        gcCount = gCount + cCount
        tmpGCContent = (float(gcCount)/len(seq))*100
        if tmpGCContent > GCContent:
            GCContent = tmpGCContent
            x=seqslist.index(seq)


    output = "%s\n%.6f" %(nameslist[x],GCContent)

    print (output)


GC_counter ("./files/rosalind_gc.txt")