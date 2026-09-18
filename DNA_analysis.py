given_seq= "ATGGGGAGCTTTATG"

pattern1 = "AGGAGG" # RBS
pattern2 = "ATG" # start codon
pattern3 = "TATAAA" # TATA box 

L2 = []
A=given_seq.count(pattern2)
for i in range(len(given_seq)) :
    if given_seq[i:i+len(pattern2)] == pattern2 :
        L2.append(i)

print("Nombre de", pattern2, " : ", A, "| positions : ", L2)