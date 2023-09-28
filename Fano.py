def fano(seqs):    if len(seqs) == 1:
        return {seqs[0]: "0"}    elif len(seqs) == 2:
        return {seqs[0]: "0", seqs[1]: "1"}    else:
        freq = {}        for seq in seqs:
            if seq in freq:                freq[seq] += 1
            else:                freq[seq] = 1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)        split_index = len(sorted_freq)//2
        lg = [x[0] for x in sorted_freq[:split_index]]        rg = [x[0] for x in sorted_freq[split_index:]]
                lc = fano(lg)
        rc = fano(rg)        
        result = {}        for seq in lc:
            result[seq] = "0" + lc[seq]        for seq in rc:
            result[seq] = "1" + rc[seq]          return result
sequence = input()
codes = fano(sequence)for seq in codes:
    print(seq + codes[seq])
