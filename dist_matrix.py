from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
import numpy as np

# Read the alignment file
alignment = AlignIO.read("/home/tolina/Desktop/CMV_data/10_sample_hcmv.fasta", "fasta")

# Initialize the calculator with the 'identity' model
calculator = DistanceCalculator('identity')

dm = calculator.get_distance(alignment)
# Get the sequence names
sequence_names = [record.id for record in alignment]

distance_matrix = np.zeros((len(sequence_names), len(sequence_names)))
for i, name1 in enumerate(sequence_names):
    for j, name2 in enumerate(sequence_names):
        distance_matrix[i, j] = dm[name1, name2]

with open("distance_matrix.txt", "w") as f:
    # Write the header
    f.write("\t" + "\t".join(sequence_names) + "\n")

    for i, name in enumerate(sequence_names):
        f.write(name + "\t" + "\t".join(map(str, distance_matrix[i])) + "\n")

