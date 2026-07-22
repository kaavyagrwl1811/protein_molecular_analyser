import pandas as pd

print(pd.__version__)

"""
Protein Molecular Analyser
------------------------------------------
A beginner-friendly tool to compute the molecular mass (in Daltons / Da)
and analyse the protein sequence
"""

AMINO_ACID_WEIGHTS = {
    'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.16,
    'E': 147.13, 'Q': 146.15, 'G': 75.07, 'H': 155.16, 'I': 131.17,
    'L': 131.17, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 97.12,
    'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
}

AMINO_ACIDS = {
    "A": "Alanine", "R": "Arginine", "N": "Asparagine", "D": "Aspartic Acid", "C": "Cysteine",
    "E": "Glutamic Acid", "Q": "Glutamine", "G": "Glycine", "H": "Histidine", "I": "Isoleucine",
    "L": "Leucine", "K": "Lysine", "M": "Methionine", "F": "Phenylalanine", "P": "Proline",
    "S": "Serine", "T": "Threonine", "W": "Tryptophan", "Y": "Tyrosine", "V": "Valine"
}


def analyze_protein():

    print("=" * 50)
    print("Protein Molecular Analyser".center(50))
    print("=" * 50)

    df = pd.DataFrame({
        "Code": AMINO_ACIDS.keys(),
        "Amino Acid": AMINO_ACIDS.values(),
        "Molecular Weight (Da)": AMINO_ACID_WEIGHTS.values()
    })

    print(df)

    protein = input("\nEnter your protein sequence: ").upper().strip()

    if len(protein) == 0:
        print("Sequence cannot be empty.")
        return

    for amino_acid in protein:
        if amino_acid not in AMINO_ACIDS:
            print(f"Invalid amino acid: {amino_acid}")
            return

    sequence_length = len(protein)
    total_weight = 0.0
    composition = {}

    for amino_acid in protein:
        total_weight += AMINO_ACID_WEIGHTS[amino_acid]

        if amino_acid in composition:
            composition[amino_acid] += 1
        else:
            composition[amino_acid] = 1

    print(f"\nProtein Sequence: {protein}")

    print("=" * 50)
    print("Amino Acid Composition".center(50))
    print("=" * 50)

    composition_df = pd.DataFrame({
        "Code": composition.keys(),
        "Amino Acid": [AMINO_ACIDS[aa] for aa in composition.keys()],
        "Count": composition.values()
    })

    print(composition_df)

    print("=" * 50)
    print("Molecular Weight".center(50))
    print("=" * 50)

    print(f"{total_weight:.2f} Da")
    print(f"{total_weight / 1000:.2f} kDa")

    print("=" * 50)
    print("Sequence Length".center(50))
    print("=" * 50)

    print(sequence_length)

    print("=" * 50)
    print("Percentage Composition".center(50))
    print("=" * 50)

    for amino_acid, count in composition.items():
        percentage = (count / sequence_length) * 100
        print(f"{amino_acid} : {count} : {percentage:.2f}%")

    peptide_bonds = sequence_length - 1
    water_loss = peptide_bonds * 18.015
    corrected_weight = total_weight - water_loss

    print("=" * 50)
    print("Corrected Molecular Weight".center(50))
    print("=" * 50)

    print("This accounts for peptide bond formation,")
    print("where one water molecule is released per peptide bond.\n")

    print(f"Peptide Bonds : {peptide_bonds}")
    print(f"Water Loss    : {water_loss:.2f} Da")
    print(f"Corrected Weight : {corrected_weight:.2f} Da")

    print("=" * 50)
    print("Hydrophobic and Hydrophilic Composition".center(50))
    print("=" * 50)

    hydrophobic = {'A', 'V', 'I', 'L', 'M', 'F', 'W', 'Y', 'P'}
    hydrophilic = {'R', 'N', 'D', 'Q', 'E', 'K', 'S', 'T', 'H', 'C', 'G'}

    hydrophobic_count = 0
    hydrophilic_count = 0

    for aa in protein:
        if aa in hydrophobic:
            hydrophobic_count += 1

        if aa in hydrophilic:
            hydrophilic_count += 1

    hydrophobic_perc = (hydrophobic_count / sequence_length) * 100
    hydrophilic_perc = (hydrophilic_count / sequence_length) * 100

    print(f"Hydrophobic residues : {hydrophobic_count}")
    print(f"Hydrophilic residues : {hydrophilic_count}")

    print(f"Hydrophobic percentage : {hydrophobic_perc:.2f}%")
    print(f"Hydrophilic percentage : {hydrophilic_perc:.2f}%")

    if hydrophobic_perc > hydrophilic_perc:
        print("Protein is predominantly hydrophobic.")

    elif hydrophilic_perc > hydrophobic_perc:
        print("Protein is predominantly hydrophilic.")

    else:
        print("Protein is equally hydrophobic and hydrophilic.")


while True:
    analyze_protein()

    choice = input("\nDo you want to analyze another protein? (Y/N): ").strip().upper()

    if choice != "Y":
        print("\nThank you for using the Protein Molecular Analyser!")
        break
