############################################################################
#example defaults for practice (use command_line = False if using jupyterlab)
command_line = True
if not command_line:
    class Test:
            pass
    args = Test()
    args.infile="C:\\Users\\jamie\\OneDrive\\Desktop\\infile.txt"
    args.outfile="C:\\Users\\jamie\\OneDrive\\Desktop\\outfile.txt"
    args.label="13C"
    args.maxlabel=12

############################################################################
#### load modules ####
import argparse
import re

############################################################################
#### Parse command line arguments ####
if command_line:
    parser = argparse.ArgumentParser(
        prog='isotopeListBuilder',
        description='Add rows for isotopes automatically to each molecule for Skyline mass lists',
        epilog='Ask Jamie if you need help'
    )
    parser.add_argument('-i', '--infile') #input file (example: "infile.txt")
    parser.add_argument('-o', '--outfile') #output file name (example: "outfile.txt")
    parser.add_argument('-l', '--label') #isotope atom (example: "13C")
    args = parser.parse_args()

atomLabeled = ''.join([char for char in args.label if char.isalpha()])
isotopeNominalMass = ''.join([char for char in args.label if char.isdigit()])
mySearchPattern = atomLabeled + r'(\d*)' #using re

############################################################################
#### Line by line, read the old Skyline list and print a new mass list that contains the extra isotope rows ####
with open(args.infile, 'r', encoding="utf-8") as infile:
    with open (args.outfile, 'w', encoding='utf-8') as outfile:
        # Process header
        header = infile.readline().rstrip().split('\t')
        formulaIndex = header.index("Molecular Formula")
        adductIndex = header.index("Precursor Adduct")
        outLine = "\t".join(header)
        outfile.write(outLine + "\n")
        # Process molecules
        for my_line in infile:
            split_line = my_line.rstrip().split('\t')
            myFormula = split_line[formulaIndex]
            myMatch = re.search(mySearchPattern, myFormula)
            numberOfAtomsOfInterest = myMatch.group(1)
            numberOfAtomsOfInterest = int(numberOfAtomsOfInterest) if numberOfAtomsOfInterest else 1  # Default to 1 if no number
            outfile.write("\t".join(split_line) + "\n")
            if numberOfAtomsOfInterest < 1:
                continue
            for i in range(1, numberOfAtomsOfInterest+1):
                myAdduct = split_line[adductIndex]
                positionM = myAdduct.find("M")
                newAdduct = myAdduct[:positionM + 1] + str(i) + atomLabeled + isotopeNominalMass + myAdduct[positionM + 1:]
                newLine = split_line.copy()
                newLine[adductIndex] = newAdduct
                outfile.write("\t".join(newLine) + "\n")

print('All done!')