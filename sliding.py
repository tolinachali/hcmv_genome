import argparse
from Bio import SeqIO

def sliding_window(sequence, window_size, step_size):
    """
    Generate subsequences using a sliding window approach.

    Parameters:
        sequence (str): The input genome sequence.
        window_size (int): The size of the window.
        step_size (int): The step size for the sliding window.

    Yields:
        tuple: Start position (1-based) and sequence of the current window.
    """
    for start in range(0, len(sequence) - window_size + 1, step_size):
        yield start + 1, sequence[start:start + window_size]

def generate_sliding_windows(input_fasta, output_fasta, window_size, step_size):
    """
    Generate sliding windows for each sequence in the input FASTA file.

    Parameters:
        input_fasta (str): Path to the input FASTA file.
        output_fasta (str): Path to save the sliding window sequences.
        window_size (int): The size of the sliding window.
        step_size (int): The step size for the sliding window.

    Returns:
        None
    """
    with open(output_fasta, 'w') as out_f:
        for record in SeqIO.parse(input_fasta, "fasta"):
            for start, window_seq in sliding_window(str(record.seq), window_size, step_size):
                out_f.write(f">{record.id}_window_{start}\n{window_seq}\n")
    print(f"Sliding windows saved to {output_fasta}")

def main():
    parser = argparse.ArgumentParser(description="Generate sliding windows from a genome sequence in FASTA format.")
    parser.add_argument("-g", "--genome_fasta", required=True, help="Path to the input genome FASTA file.")
    parser.add_argument("-w", "--window_size", type=int, required=True, help="Size of the sliding window.")
    parser.add_argument("-s", "--step_size", type=int, required=True, help="Step size for the sliding window.")
    parser.add_argument("-o", "--output_fasta", required=True, help="Path to save the output sliding windows FASTA file.")

    args = parser.parse_args()

    generate_sliding_windows(args.genome_fasta, args.output_fasta, args.window_size, args.step_size)

if __name__ == "__main__":
    main()
