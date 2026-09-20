import streamlit as st
from DNA_analysis import find_pattern, codon_dic, find_AA

st.title("DNA Sequence Analyzer")
sequence = st.text_area("Paste your DNA sequence here:")
rbs = st.checkbox("RBS") #la checkbox renvoie true si elle est cochée et false sinon
if rbs == True :
    result_rbs = find_pattern(sequence, "AGGAGG")
    st.write(result_rbs)

TATA_box = st.checkbox("TATA box")
if TATA_box == True :
    result_TATA = find_pattern(sequence, "TATAAA")
    st.write(result_TATA)

start_codon = st.checkbox("Start codon")
if start_codon == True :
    result_start = find_pattern(sequence, "ATG")
    st.write(result_start)

stop_codon = st.checkbox("Stop codon")
amino_acid = st.checkbox("Amino acid")

if stop_codon == True :
    stop_codon_choice = st.multiselect("Choose stop codons:", ["TAA", "TAG", "TGA"])
    for stop in stop_codon_choice :
        result_stop = find_pattern(sequence, stop)
        st.write(result_stop)

if amino_acid == True :
    amino_acid_choice = st.multiselect("Choose amino acids:", list(codon_dic.keys()))
    Rf = st.radio("Choose reading frame:", [1, 2, 3])
    for AA in amino_acid_choice :
        result_amino_acid_choice = find_AA(sequence, Rf, AA)
        st.write(result_amino_acid_choice)