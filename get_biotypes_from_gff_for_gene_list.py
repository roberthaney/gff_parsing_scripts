import sys
import re
import argparse

genes = {}

# parse arguments in command line interface
prog_parser = argparse.ArgumentParser(prog="get_biotypes_from_gff_for_gene_list.py", usage="%(prog)s gene_list_filename gff_filename output_filename")
prog_parser.add_argument("<Filename of gene list file>", type=str)
prog_parser.add_argument("<Filename of gff file>", type=str)
prog_parser.add_argument("<Filename of output file>", type=str)
args = prog_parser.parse_args()

# open file containing list of gene names, one per line
with open(sys.argv[1]) as fhand:
	for line in fhand:
		if line.rstrip() not in genes:
			genes[line.rstrip()] = ""

# keep count of number of biotypes found to compare to number of genes
counter = 0
# open gff file
with open(sys.argv[2]) as fhand:
	for line in fhand:
		# skip comment lines
		if line.startswith("#"):
			continue
		items = line.split()
		# check if gene in list and find name and biotype
		if items[2] == "gene":
			name = re.findall("ID=gene-(\S+);Dbxref", line)[0]
			if name in genes:
				biotype = (re.findall("gene_biotype=(\S+)",line)[0]).split(";")[0]
				genes[name] = biotype
				counter += 1

print "Found biotypes for", counter, "genes of", len(genes), "in file"

with open(sys.argv[3], "w") as fhand_out:
	for gene in genes:
		fhand_out.write(gene + "\t" + genes[gene] + "\n")
