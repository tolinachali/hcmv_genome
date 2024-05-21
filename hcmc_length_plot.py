

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/tolina/Desktop/hcmv_genome/hcmv_sequence.tsv', sep='\t')

print(df)

df = df[df['Sequence Length'] > 10000]  # Removing the entry with length 236 as it seems to be an outlier

plt.figure(figsize=(10, 6))
plt.hist(df['Sequence Length'], bins=20, edgecolor='black')
plt.title('Frequency Distribution of HCMV Genome Sequence Lengths')
plt.xlabel('Sequence Length (bp)')
plt.ylabel('Frequency')
plt.grid(True)

min_length = df['Sequence Length'].min()
max_length = df['Sequence Length'].max()
plt.text(min_length, 100, f'Minimum Length: {min_length} bp', ha='left', va='bottom', color='green')
plt.text(max_length, 100, f'Maximum Length: {max_length} bp', ha='right', va='bottom', color='green')

plt.savefig("tsv_plot.png")
