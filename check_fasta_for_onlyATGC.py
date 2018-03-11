#this scirpt runs thruogh a fasta file to confrim only ATGC nucleotide are present in the sequences. If there are other it will print them to a list
#
import sys

#open the lists and leave blank
samples=[]
seq=[]
#open the input fasta file
with open(sys.argv[1],"r") as fasta_in:
	#look at all lines in the input fasta
	for lines in fasta_in:
		#in std fasta if line has > count as a sample		
		if lines.startswith(">"):
			samples.append(lines.strip())
		#if line doesn't start with > count as a sequence line
		else:
			seq=list(lines.strip())

#specify only nucliotides 
code=['A','T','G','C']


# look for non-nucleotide sequences and print them as STDOUT
if not code in seq:
	print seq

print "Done!"
