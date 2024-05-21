from Bio import SeqIO

input_file = '/home/tolina/Desktop/my_research/hcmv_raw_data/hcmv_sequence.gb'
output_file = 'hcmv_sequence.tsv'

with open(output_file, 'w') as tsv_file:
    # Write the header
    tsv_file.write('Accession\tSequence Length\n')
    for record in SeqIO.parse(input_file, 'genbank'):
        accession = record.id
        sequence_length = len(record.seq)
        # Write the information to the TSV file
        tsv_file.write(f'{accession}\t{sequence_length}\n')

print(f'Conversion complete. Data saved to {output_file}')
