🧬 Protein Molecular Analyser

A Python-based bioinformatics application for analyzing protein sequences and computing molecular properties using computational biology principles.

<p align="center">










</p>
🌟 Why this project?

Proteins are the workhorses of every living cell. Understanding their molecular properties is fundamental in biotechnology, molecular biology, drug discovery, and bioinformatics.

This project demonstrates how Python can be used to transform a raw amino acid sequence into meaningful biochemical information by applying real scientific principles such as molecular weight calculation, peptide bond correction, amino acid composition analysis, and hydrophobicity assessment.

Rather than being a simple calculator, this project serves as a miniature bioinformatics toolkit for beginners.

✨ Features
Feature	Description
✅ Sequence Validation	Detects invalid amino acid symbols
🧬 Molecular Weight	Calculates total molecular mass (Da & kDa)
💧 Peptide Bond Correction	Accounts for water molecules released during peptide bond formation
📊 Amino Acid Composition	Displays residue counts using Pandas
📈 Percentage Composition	Calculates abundance of every amino acid
📏 Sequence Length	Reports total protein length
🌊 Hydrophobicity Analysis	Estimates hydrophobic vs hydrophilic composition
🔁 Multiple Analyses	Analyze unlimited protein sequences without restarting
⚙️ Technologies
Technology	Purpose
Python	Core programming language
Pandas	Data visualization using DataFrames
Dictionaries	Amino acid lookup tables
Functions	Modular program structure
Loops	Sequence traversal
Conditional Statements	Validation and analysis
Bioinformatics Principles	Biological computations
🧬 Scientific Concepts Implemented

This project incorporates several fundamental concepts used in computational biology:

Protein sequence validation
Amino acid molecular masses
Protein molecular weight calculation
Peptide bond formation
Water loss correction
Amino acid frequency analysis
Percentage abundance
Hydrophobic vs hydrophilic residue analysis
⚗️ Methodology
1️⃣ Validate Sequence

The program first verifies that every character belongs to one of the 20 standard amino acids.

2️⃣ Calculate Molecular Weight

Each amino acid contributes its molecular mass.

Total Weight = Σ Individual Amino Acid Weights
3️⃣ Correct for Peptide Bond Formation

During protein synthesis,

Every peptide bond releases one molecule of water (18.015 Da).

Therefore,

Corrected Weight =
Σ Amino Acid Weights
−
(Number of Peptide Bonds × 18.015 Da)
4️⃣ Composition Analysis

The occurrence of every amino acid is counted and displayed in a Pandas DataFrame.

5️⃣ Hydrophobicity Analysis

Residues are classified as

Hydrophobic
Hydrophilic

to estimate the overall biochemical nature of the protein.

📂 Project Structure
Protein-Molecular-Analyser/

│── protein_analyser.py
│── README.md
│── requirements.txt
🚀 Getting Started

Clone the repository

git clone https://github.com/yourusername/Protein-Molecular-Analyser.git

Move into the project directory

cd Protein-Molecular-Analyser

Install dependencies

pip install pandas

Run

python protein_analyser.py
📷 Example
Input
MKWVTFISLL
Output
Protein Sequence
MKWVTFISLL

Sequence Length
10

Molecular Weight
1204.34 Da

Corrected Molecular Weight
1042.21 Da

Hydrophobic Composition
70%

Hydrophilic Composition
30%

Classification
Predominantly Hydrophobic
📊 Workflow
Protein Sequence
        │
        ▼
Sequence Validation
        │
        ▼
Weight Calculation
        │
        ▼
Peptide Bond Correction
        │
        ▼
Composition Analysis
        │
        ▼
Hydrophobicity Analysis
        │
        ▼
Final Report
🎯 Learning Outcomes

This project strengthened practical skills in:

Python Programming
Computational Biology
Bioinformatics
Data Structures
Scientific Computing
User Input Validation
Algorithm Design
Clean Code Practices
🔮 Roadmap

Future improvements include:

FASTA file support
CSV/Excel export
Protein isoelectric point (pI)
Instability Index
Aromaticity
GRAVY score
Extinction coefficient
Molecular formula
Streamlit web interface
Tkinter GUI
Protein visualization
Batch sequence analysis
DNA → Protein translation
🤝 Contributing

Contributions are welcome!

If you have ideas for improving the project, feel free to fork the repository, open an issue, or submit a pull request.

📜 License

This project is released under the MIT License.

👩‍💻 Author

Kaavya Agarwal

Aspiring Biotechnology Engineer | Bioinformatics Enthusiast | Python Developer

<p align="center">
⭐ If you found this project useful, consider giving it a star!

Built with Python 🐍 • Inspired by Bioinformatics 🧬

</p>
