
## import the libraries
import streamlit as st 
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from Bio.SeqUtils.ProtParam import ProteinAnalysis

## title and input
st.title("Amino acids counter")

if st.button ("**Show me amino acids**", use_container_width = True):
    st.write ("""
            **Cationic** aa: **R, H, K** \n
            **Lipophilic** aa: **F, I, L, A, M, V, P, T** \n
            **Other** aa: **G, Y, W, Q, E, N, D, S, C**""")
else:
    st.success("🤔 If you want to know exact what is **Cationic**, **Lipophylic** and **Other amino acids** click above ⬆️")

first_input = st.text_input("**Give me a name**")
second_input = st.text_input("**Paste amino acid sequence**")
st.write("**Peptide name is**", first_input)
st.write("**Sequence you give me is**", second_input)
st.set_option('deprecation.showPyplotGlobalUse', False)


## calculating the amount of amino acids
if second_input != "":
    protein = ProteinAnalysis(second_input)
    aa_composition = protein.count_amino_acids()
    cationic_aa = ['R', 'H', 'K']
    cationic_count = sum([aa_composition[aa] for aa in cationic_aa])
    hydrophobic_aa = ['F', 'I', 'L', 'A', 'M', 'V', 'P', 'T']
    hydrophobic_count = sum([aa_composition[aa] for aa in hydrophobic_aa])
    other_aa = ['G', 'Y', 'W', 'Q', 'E', 'N', 'D', 'S', 'C']
    other_count = sum([aa_composition[aa] for aa in other_aa])
    total_count = sum(aa_composition.values())
    st.write ("Amount of cationic amino acids: ", cationic_count)
    st.write("Amount of lipophilic amino acids: ", hydrophobic_count)
    st.write("Amount of other amino acids: ", other_count)
    st.write("Molecular mass of peptide:", "%0.2f" % protein.molecular_weight(), "G/mol")
## calculating the percentage of amino acids
    if total_count > 0:
        cationic_percentage = cationic_count / total_count * 100
        hydrophobic_percentage = hydrophobic_count / total_count * 100
        other_percentage = other_count / total_count * 100
        st.write("Percentage of cationic amino acids: ", round(cationic_percentage, 2), "%")
        st.write("Percentage of lipophilic amino acids: ", round(hydrophobic_percentage, 2), "%")
        st.write("Percentage of other amino acids: ", round(other_percentage, 2), "%")
        if other_percentage > 0:
            def my_df():
                data = [["Cationic", cationic_count], ["Lipophylic", hydrophobic_count], ["Other", other_count]] 
                df = pd.DataFrame (data, columns = ["Amino acids", "Number of amino acids"])
                x_values = df["Amino acids"]
                y_values = df["Number of amino acids"]
                colors = ['skyblue', 'lightgreen', 'lightcoral']
                plt.figure(figsize=(9, 4))
                plt.bar(x_values, y_values, color = colors)
                plt.xlabel("Amino acids")
                plt.ylabel("Number of amino acids")
                plt.title(first_input)    
                st.pyplot()
            if cationic_count > 0:
                my_df()

        

