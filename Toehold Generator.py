seq = input("Enter the MiRNA you want to target:").upper()

# Helper variable
# REVerse COMPlimentary sequence
revcomp = ""

for i in seq:
    if i == "A": revcomp += "U"
    if i == "U": revcomp += "A"
    if i == "C": revcomp += "G"
    if i == "G": revcomp += "C"

# Reverses the string
revcomp = revcomp[::-1]

yside = ""

# Retrieves 10 characters of the reverse complimentary sequence for one of the two customized sections of the final RNA
for i in revcomp[-10:]:
    if i == "A": yside += "U"
    if i == "U": yside += "A"
    if i == "C": yside += "G"
    if i == "G": yside += "C"


# Inserts customized portions into the proven toehold sequence boilerplate
final = "GGG" + revcomp[-21:] + "AUGAUUGUAAACAGAGGAGAUACAAUAUG" +\
        yside + "ACCUGGCGGCAGCGCAAAAGAUGCGUAAA"

print(final)
