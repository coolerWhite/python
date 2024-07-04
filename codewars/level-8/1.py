# def dna_to_rna(dna):
#     while "T" in dna:
#         word = ""
#         for i in dna:
#             if i == "T":
#                 word += "U"
#         return print(word)

def dna_to_rna(dna):
    return dna.replace("T", "U")

dna_to_rna("TTTT")