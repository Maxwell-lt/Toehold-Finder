seq = input("Enter the MiRNA you want to target:").upper()

revcomp = ""

for i in seq:
    if i == "A": revcomp += "U"
    if i == "U": revcomp += "A"
    if i == "C": revcomp += "G"
    if i == "G": revcomp += "C"

revcomp = revcomp[::-1]

yside = ""

for i in revcomp[-10:]:
    if i == "A": yside += "U"
    if i == "U": yside += "A"
    if i == "C": yside += "G"
    if i == "G": yside += "C"


final = "GGG" + revcomp[-21:] + "AUGAUUGUAAACAGAGGAGAUACAAUAUG" +\
        yside + "ACCUGGCGGCAGCGCAAAAGAUGCGUAAA"

print(final)
