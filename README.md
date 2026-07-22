# 🧬 Protein Molecular Analyser

A Python-based bioinformatics tool that analyzes protein sequences and computes their molecular properties using fundamental principles of computational biology.

The application validates protein sequences, calculates molecular weight, accounts for peptide bond formation, determines amino acid composition, and evaluates the hydrophobic and hydrophilic nature of proteins.

This project demonstrates how Python can be applied to solve real biological problems through computational analysis.

---

## 📸 Screenshots

### 🧬 Home Screen

*(Add a screenshot here after running the program.)*

```text
==========================================
        Protein Molecular Analyser
==========================================
```

---

### 📊 Amino Acid Composition

*(Add screenshot here)*

---

### ⚖️ Molecular Weight Analysis

*(Add screenshot here)*

---

### 🌊 Hydrophobicity Analysis

*(Add screenshot here)*

---

## ✨ Features

- 🧬 Validates protein sequences containing the 20 standard amino acids
- ⚖️ Calculates protein molecular weight in Daltons (Da)
- 📏 Converts molecular weight into kiloDaltons (kDa)
- 💧 Corrects molecular weight by accounting for peptide bond formation
- 📊 Displays amino acid composition using a Pandas DataFrame
- 📈 Calculates percentage abundance of each amino acid
- 📐 Determines protein sequence length
- 🌊 Calculates hydrophobic and hydrophilic residue composition
- 🔁 Allows continuous analysis of multiple protein sequences
- 🧪 Provides biologically meaningful interpretation of the protein

---

## 🧠 Biological Workflow

```text
Protein Sequence
        │
        ▼
Sequence Validation
        │
        ▼
Molecular Weight Calculation
        │
        ▼
Peptide Bond Correction
        │
        ▼
Amino Acid Composition
        │
        ▼
Percentage Composition
        │
        ▼
Hydrophobicity Analysis
        │
        ▼
Final Report
```

---

## 🧪 Analyses Performed

| Analysis | Description |
|----------|-------------|
| Sequence Validation | Ensures only valid amino acids are present |
| Molecular Weight | Calculates total molecular mass |
| Peptide Bond Correction | Accounts for water loss during peptide bond formation |
| Sequence Length | Determines the number of amino acids |
| Amino Acid Composition | Counts occurrences of each amino acid |
| Percentage Composition | Calculates abundance of each residue |
| Hydrophobicity Analysis | Classifies the protein based on residue composition |

---

## 🧬 Example Run

### Input

```text
Enter your protein sequence:

MKWVTFISLLFLFSSAYSR
```

### Output

```text
==================================================
Protein Molecular Analyser
==================================================

Protein:
MKWVTFISLLFLFSSAYSR

Sequence Length
19

Molecular Weight
2295.52 Da

Corrected Molecular Weight
1971.25 Da

Hydrophobic Residues
63.16%

Hydrophilic Residues
36.84%

Protein is predominantly hydrophobic.
```

---

## 🧬 Understanding the Results

- **Protein Sequence** displays the user-provided amino acid sequence.
- **Sequence Length** represents the total number of amino acid residues.
- **Molecular Weight** is calculated by summing the molecular masses of all amino acids.
- **Corrected Molecular Weight** subtracts the mass of water molecules released during peptide bond formation.
- **Amino Acid Composition** shows the frequency of each amino acid.
- **Percentage Composition** indicates the relative abundance of each residue.
- **Hydrophobicity Analysis** estimates whether the protein is predominantly hydrophobic or hydrophilic.

---

## ⚙️ Technologies Used

- 🐍 Python 3
- 📊 Pandas
- 🧬 Bioinformatics concepts
- 📚 Dictionaries
- 🔄 Loops and Conditional Statements
- 🧮 Functions
- 🧪 Protein Chemistry Principles

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/protein_molecular_analyser.git
```

### 2. Navigate to the project directory

```bash
cd protein_molecular_analyser
```

### 3. Install the required dependency

```bash
pip install pandas
```

### 4. Run the program

```bash
python protein_analyser.py
```

### 5. Enter a protein sequence when prompted.

---

## 📚 Scientific Concepts Demonstrated

- Protein sequence validation
- Amino acid molecular weights
- Protein molecular weight calculation
- Peptide bond formation
- Water loss correction
- Amino acid composition analysis
- Percentage abundance calculation
- Hydrophobic vs Hydrophilic residue classification
- Computational protein analysis

---

## 🎯 Learning Outcomes

This project helped strengthen my understanding of:

- Python programming
- Bioinformatics fundamentals
- Protein chemistry
- Scientific computing
- Data structures and algorithms
- User input validation
- Data analysis using Pandas
- Computational biology workflows

---

## 🚀 Future Improvements

- 📂 FASTA file support
- 📊 Export results to CSV and Excel
- 📈 Graphical amino acid composition charts
- 🧪 Protein isoelectric point (pI) calculation
- 💧 GRAVY (Grand Average of Hydropathicity) score
- 🧬 Instability Index
- 🧪 Aromaticity calculation
- 🖥️ GUI using Tkinter
- 🌐 Streamlit web application
- 📦 Batch protein analysis

---

## 👩‍💻 Author

**Kaavya Agarwal**

Aspiring Biotechnology Engineer passionate about **Bioinformatics, Computational Biology, Data Science, and Python Programming.**

---

## 📜 License

This project is licensed under the **MIT License**.

---

# ⭐ If you found this project interesting, consider giving the repository a star and following my bioinformatics journey!
