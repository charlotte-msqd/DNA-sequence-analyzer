pattern1 = "AGGAGG" # RBS
pattern2 = "ATG" # start codon
pattern3 = "TATAAA" # TATA box 


def find_pattern (sequence, pattern) :
    L = []
    A=sequence.count(pattern)
    for i in range(len(sequence)) :
        if sequence[i:i+len(pattern)] == pattern :
            L.append(i + 1)
    return (f"Found {pattern}: {A} times | positions : {L}")


codon_dic = {"Phe": ["TTT", "TTC"],
    "Leu": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
    "Ile": ["ATT", "ATC", "ATA"],
    "Met": ["ATG"],
    "Val": ["GTT", "GTC", "GTA", "GTG"],
    "Ser": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "Pro": ["CCT", "CCC", "CCA", "CCG"],
    "Thr": ["ACT", "ACC", "ACA", "ACG"],
    "Ala": ["GCT", "GCC", "GCA", "GCG"],
    "Tyr": ["TAT", "TAC"],
    "His": ["CAT", "CAC"],
    "Gln": ["CAA", "CAG"],
    "Asn": ["AAT", "AAC"],
    "Lys": ["AAA", "AAG"],
    "Asp": ["GAT", "GAC"],
    "Glu": ["GAA", "GAG"],
    "Cys": ["TGT", "TGC"],
    "Trp": ["TGG"],
    "Arg": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Gly": ["GGT", "GGC", "GGA", "GGG"],
    "Stop": ["TAA", "TAG", "TGA"]}


def find_AA (sequence, RF, AA) :
    i = RF - 1
    L =[]
    A = 0
    while i + 3 <= len(sequence) :
        if sequence[i:i+3] in codon_dic[AA] :
            L.append(i + 1)
            A = A + 1
        i = i + 3
    return (f"Found {AA}: {A} times | positions : {L}")
