ref_seq = ""
acc = acc_cal(ref_seq)
header = build_occ_header(ref_seq, )


input_reads = [] # list of strings

def wc_comp(seq):
    compliment = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([compliment[seq[len(seq) - i -1]] for i in range(len(seq))])

def acc_cal(seq):
    acc = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(seq):
        acc[seq[i]] += 1
    acc['C'] += acc['A']
    acc['G'] += acc['C']
    acc['T'] += acc['G']
    return acc

def build_occ_header(seq, header_size):
    header = [[{'A': 0, 'C': 0, 'G': 0, 'T': 0}]] # list of dictionaries
    for i in range(1, len(seq)/header_size):
        header[i] = header[i-1]
        for j in range(header_size):
            header[i][seq[i*header_size+j]] += 1
    return header

def occ_cal(seq, header, header_size):
    pass

def occur(base, idx):
    occ_cal(seq, header, header_size)

def bwt():
    pass

def backwardExt(biIntv, base):
    # bi-interval: [Il(Y ), Il(Y_), Is(Y )]
    # Σ = {$, A, C, G, T, N}
    k = s = l = [0] * 6
    for b in range(6):
        k[b] = acc[b] + occur(b, biIntv[0] - 1)
        s[b] = occur(b, biIntv[0] + biIntv[2] - 1) - occur(b, biIntv[0] - 1)
    l[0] = biIntv.[1]
    l[4] = l[0] + s[0]
    for b in range(3,0,-1):
        l[b] = l[b+1] + s[b+1]
    l[5] = l[1] + s[1]

    return [k[base], l[base], s[base]]

def forwardExt(biIntv, base):
    compliment = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    [L, K, S] = backwardExt([biIntv[1], biIntv[0], biIntv[2]], compliment[base])
    return [K, L, S]

def diff(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

# Seed generation
def smem_gen(read, init_pos):
    pingIntv, pongIntv, outIntv = []
    intv = [acc[read[init_pos]], acc[comp[read[init_pos]]], acc[read[init_pos] + 1] - acc[read[init_pos]]]
    # forward extensions
    for i in range(init_pos, len(read)):
        newIntv = forwardExt(intv, read[i])
        if diff(newIntv, intv):
            pingIntv.append(newIntv) # push to pingIntv
        elif newIntv[2] <= 0: # noMoreMatch
            break
        intv = newIntv

    # swap pingIntv and pongIntv
    pongIntv = pingIntv
    pingIntv = []

    # backward extensions
    for i in range(init_pos-1, -1, -1):
        pingIntv = []
        for intv in pongIntv:
            newIntv = backwardExt(intv, read[i])
            if newIntv[2] <= 0 or i == -1:
                outIntv.append(newIntv)
            elif extendable():
                pingIntv.append(newIntv)
        if not pingIntv: # empty list
            break
        # swap pingIntv and pongIntv
        pongIntv = pingIntv
    # Output: A set of SMEMs that contains the character in init_pos.
    return outIntv

# suffix array lookup
def suffix_array():
    pass

# Seed extension
def sw_align():
    # https://gist.github.com/radaniba/11019717
    pass
