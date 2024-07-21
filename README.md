7-20-2024

isotopeListBuilder.py is a small program to automatically add all possible isotopes to a Skyline mass list lacking isotope addcuts, for Stable Isotope Labeling (SIL) experiments. The user should then edit the output for biologic sense and Skyline integration efficiency.

############################################################################

INSTALLATION

- python version 3: can be downloaded from www.python.org/downloads
- isotopeListBuilder.py: from this repository

############################################################################

SETUP

Make an infile.txt that is a tab-delimited file of what you would normally import to Skyline without any isotopes.

Make sure there is a column exactly named "Molecular Formula" and a column exactly named "Precursor Adduct". These are the only required columns.

An example is included in this repository, and a few lines of an example are below:
Molecule List Name | Molecule Name | Molecular Formula | Precursor Adduct | Precursor Charge | Explicit Retention Time | Explicit Retention Time Window | Note
--- | --- | --- | --- | --- | --- | --- | ---
Amino acid | Alanine | C3H7NO2 | M-H | -1 | 10.79 | 1 | sarcosine isobar
Glycolysis | 2PG | C3H7O7P | M-H | -1 | 12.342 | 1 | unlikely to distinguish from isobar 2-PG
PPP | 6-Phospho-D-gluconate | C6H13O10P | M-H | -1 | 12.872 | 1 |

Know these in advance:

- The path and name of this infile
- Which label you are tracing (13C, 15N, 2H, 18O, etc.)
- The path and filename you want for the outfile

############################################################################

USAGE

Open a terminal and cd to the directory containing isotopeListBuilder.py.

*Windows (command terminal):*

Full paths written out:

```
python -m isotopeListBuilder --infile="C:\\Users\\jamie\\OneDrive\\Desktop\\infile.txt" --outfile="C:\\Users\\jamie\\OneDrive\\Desktop\\outfile.txt" --label="13C"
```

If everything is in the same directory:

```
python -m isotopeListBuilder --infile="infile.txt" --outfile="outfile.txt" --label="13C"
```

*Mac/Linux (terminal):*

Full paths written out:

```
python -m isotopeListBuilder --infile="/Users/jamie/OneDrive/Desktop/infile.txt" --outfile="/Users/jamie/OneDrive/Desktop/outfile.txt" --label="13C"
```

If everything is in the same directory:

```
python -m isotopeListBuilder --infile="infile.txt" --outfile="outfile.txt" --label="13C"
```

An example outfile.txt is including in this repository and is below for the example above:
Molecule List Name | Molecule Name | Molecular Formula | Precursor Adduct | Precursor Charge | Explicit Retention Time | Explicit Retention Time Window | Note
--- | --- | --- | --- | --- | --- | --- | ---
Amino acid | Alanine | C3H7NO2 | M-H | -1 | 10.79 | 1 | sarcosine isobar
Amino acid | Alanine | C3H7NO2 | M13C1-H | -1 | 10.79 | 1 | sarcosine isobar
Amino acid | Alanine | C3H7NO2 | M13C213C1-H | -1 | 10.79 | 1 | sarcosine isobar
Amino acid | Alanine | C3H7NO2 | M13C313C213C1-H | -1 | 10.79 | 1 | sarcosine isobar
Glycolysis | 2PG | C3H7O7P | M-H | -1 | 12.342 | 1 | unlikely to distinguish from isobar 2-PG
Glycolysis | 2PG | C3H7O7P | M13C1-H | -1 | 12.342 | 1 | unlikely to distinguish from isobar 2-PG
Glycolysis | 2PG | C3H7O7P | M13C213C1-H | -1 | 12.342 | 1 | unlikely to distinguish from isobar 2-PG
Glycolysis | 2PG | C3H7O7P | M13C313C213C1-H | -1 | 12.342 | 1 | unlikely to distinguish from isobar 2-PG
PPP | 6-Phospho-D-gluconate | C6H13O10P | M-H | -1 | 12.872 | 1
PPP | 6-Phospho-D-gluconate | C6H13O10P | M13C1-H | -1 | 12.872 | 1
PPP | 6-Phospho-D-gluconate | C6H13O10P | M13C213C1-H | -1 | 12.872 | 1
PPP | 6-Phospho-D-gluconate | C6H13O10P | M13C313C213C1-H | -1 | 12.872 | 1
PPP | 6-Phospho-D-gluconate | C6H13O10P | M13C413C313C213C1-H | -1 | 12.872 | 1
PPP | 6-Phospho-D-gluconate | C6H13O10P | M13C513C413C313C213C1-H | -1 | 12.872 | 1
PPP | 6-Phospho-D-gluconate | C6H13O10P | M13C613C513C413C313C213C1-H | -1 | 12.872 | 1

