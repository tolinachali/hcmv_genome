from Bio import SeqIO

input_file = "/home/tolina/Desktop/CMV_data/5_lab_strains.gb"
output_file = "5_lab_strain.fasta"

# Open input and output files
with open(input_file, "r") as in_handle, open(output_file, "w") as out_handle:
    # Parse GenBank file and write sequences to FASTA file
    SeqIO.convert(in_handle, "genbank", out_handle, "fasta")

print(f"FASTA file saved as {output_file}")


