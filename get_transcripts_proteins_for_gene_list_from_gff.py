import re

fhand_gene = open("Pt2.0_rna_edgeR.ovary_common_downregulated_genes.txt")
fhand_gff = open("GCF_000365465.2_Ptep_2.0_genomic.gff")
fhand_out = open("Pt2.0_rna_edgeR.ovary_common_downregulated_protein_coding_gene_products.txt", "w")
fhand_out_prot_list = open("Pt2.0_rna_edgeR.ovary_common_downregulated_protein_coding_gene_protein_list.txt", "w")

list_genes = {}
genes = {}
transcripts = {}
found_prots = []

# save list of genes to get information for
for line in fhand_gene:
	gene = line.rstrip()
	list_genes[gene] = ""

for line in fhand_gff:
# skip comment lines
	if line.startswith("#"):
		continue
	temp = line.split()
	# check for protein coding features via CDS entries
	if temp[2] == "CDS":
		# for cds entry get gene ID and check if in list
		gene = re.findall("gene=(LOC\d+)", line)[0]
		if gene in list_genes: 
			# get protein and transcript IDs
			protein = re.findall("ID=cds-(\S+);Parent", line)[0]
			transcript = re.findall("Parent=rna-(\S+);Dbxref", line)[0]
			# multiple CDS entires possible for each protein, only get information once for each protein
			if protein not in found_prots:
				found_prots.append(protein)	
				# genes can have multiple transcripts/proteins, save as list of tuples
				if gene in genes:
					genes[gene].append((transcript, protein))
				else:
					genes[gene] = []
					genes[gene].append((transcript, protein))

print "Protein-coding genes found:", len(genes)
print "Genes in list:", len(list_genes)

# write header to file
#fhand_out.write("Gene" + "\t" + "Transcript" + "\t" + "Protein" + "\n")

mulitple_transcript_counter = 0
outcounter = 0 

# write transcripts and proteins for gene to output table
for gene in genes:
	outcounter += 1
	fhand_out.write(gene)
	# keep track of number of multiple transcript genes
	if len(genes[gene]) > 1:
		mulitple_transcript_counter += 1
	# write info for all transcript/protein pairs per gene
	for item in genes[gene]:
		fhand_out.write("\t" + item[0] + "\t" + item[1])	
	fhand_out.write("\n")

# write list of proteins to separate file
for prot in found_prots:
	fhand_out_prot_list.write(prot + "\n")


print "Printed information for", outcounter, "genes to file"
print mulitple_transcript_counter, "genes with multiple transcripts"
print "Proteins in list:", len(found_prots)
#print "Transcripts identified:", len(transcripts)

