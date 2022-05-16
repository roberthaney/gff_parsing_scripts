import re

fhand_gene = open("Pt2.0_rna_edgeR.ovary_common_upregulated_genes.txt")
fhand_gff = open("GCF_000365465.2_Ptep_2.0_genomic.gff")
fhand_out = open("Pt2.0_rna_edgeR.ovary_common_upregulated_gene_products.txt", "w")

list_genes = {}
genes = {}
transcripts = {}
found_prots = []

for line in fhand_gene:
	gene = line.rstrip()
	list_genes[gene] = ""

for line in fhand_gff:
	if line.startswith("#"):
		continue
	temp = line.split()
	if temp[2] == "CDS":
		protein = re.findall("ID=cds-(\S+);Parent", line)[0]
		if protein not in found_prots:
			found_prots.append(protein)	
			transcript = re.findall("Parent=rna-(\S+);Dbxref", line)[0]
			gene = re.findall("gene=(LOC\d+)", line)[0]
			if gene in list_genes: 
				if gene in genes:
					genes[gene].append((transcript, protein))
				else:
					genes[gene] = []
					genes[gene].append((transcript, protein))

print "Genes found:", len(genes)
print "Genes in list:", len(list_genes)

# write header to file
#fhand_out.write("Gene" + "\t" + "Transcript" + "\t" + "Protein" + "\n")

mulitple_transcript_counter = 0
outcounter = 0 
for gene in genes:
	outcounter += 1
	fhand_out.write(gene)
	if len(genes[gene]) > 1:
		#print len(genes[gene]), gene
		mulitple_transcript_counter += 1
	for item in genes[gene]:
		fhand_out.write("\t" + item[0] + "\t" + item[1])	
	fhand_out.write("\n")


print "Printed information for", outcounter, "genes to file"
print mulitple_transcript_counter, "genes with multiple transcripts"
print "Proteins in list:", len(found_prots)
#print "Transcripts identified:", len(transcripts)

