#!/usr/bin/env python3

from sys import argv

def GenerateToehold(mirna):
    """
    Finds an RNA sequence that will unfold in the presence of the MiRNA sequence given as an argument.
    
    The format of the given string should consist of only the characters 'A', 'U', 'C', and 'G'. Any other character will be ignored.
    Do not use 'T' in place of 'U'; the script will not make the conversion automatically.
    """
# Helper variable
# REVerse COMPlimentary sequence
    revcomp = ""

    for i in mirna.upper():
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
    
    return final


if __name__ == "__main__":
    if argv[1] == '-s':
        # If run from the command line with the '-s' flag, use the following sequence to generate a toehold switch.
        print(GenerateToehold(argv[2]))
    else if argv[1] == '-h' or argv[1] == '--help':
        # If a help flag is passed as the first argument, return usage information
        print("Usage:\n {0} [-s 'MiRNA sequence']".format(argv[0]))
    else:
        # If run from the command line with no options or if run from a file explorer
        seq = input("Enter the MiRNA sequence you want to target:")
        print(GenerateToehold(seq))
        # Prevent window from closing if run from a file explorer
        input("Press enter to quit...")
    
