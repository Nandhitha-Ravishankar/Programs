def MismatchFreqKmer(pattern):
    sequence=pattern
    def approx(kmer, substring, k, n):
	    count = 0
	    for i in range(k):
		    if substring[i] != kmer[i]:
			    count += 1
		    if count > n:
			    return False
	    return True

    k = int(input("What is the length of k-mer? "))
    n = int(input("What is the maximum number of mismatches? "))

    DNA = str(sequence.upper())

    counts = {}

    for i in range(0, len(DNA) - k + 1):
	    kmer = DNA[i:i + k]
	    if kmer in counts:
		    counts[kmer] += 1
	    else:
		    counts[kmer] = 1

    updateCounts = {}

    for a in counts:
	    c = 0
	    for b in counts:
		    if approx(a, b, k, n):
			    c += counts.get(b)
	    updateCounts[a] = c

    #print(updateCounts)

    frequent = max(updateCounts.values())

    ans = []
    for k in updateCounts:
	    if updateCounts[k] == frequent:
		    ans.append(k)

    output = ' '.join(ans)
    print(" ")
    print(output)

pattern="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTG"
print(MismatchFreqKmer(pattern))