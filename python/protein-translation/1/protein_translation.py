from typing import List

cp = {}
cp["AUG"] = "Methionine"
cp["UGG"] = "Tryptophan"
cp["UUA"], cp["UUG"] = "Leucine", "Leucine"
cp["UAU"], cp["UAC"] = "Tyrosine", "Tyrosine"
cp["UGU"], cp["UGC"] = "Cysteine", "Cysteine"
cp["UUU"], cp["UUC"] = "Phenylalanine", "Phenylalanine"
cp["UCU"], cp["UCC"], cp["UCA"], cp["UCG"] = "Serine", "Serine", "Serine" ,"Serine"
cp["UAA"], cp["UAG"], cp["UGA"] = "STOP", "STOP", "STOP"

# Translating RNA sequences into proteins
def proteins(strand : str) -> list[str]:
    Proteins = []
    for i in range(0,len(strand), 3):
        Protein = cp[strand[i:i+3]]
        if Protein == "STOP":
            break
        Proteins.append(Protein)
    return Proteins
