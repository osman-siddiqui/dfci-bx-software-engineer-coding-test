def find_most_frequent_sequences(file_path):
    sequences = []

    with open(file_path, "r") as file:
        current_sequence = ""
        for line in file:
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = ""
            else:
                current_sequence += line.strip()

        if current_sequence:
            sequences.append(current_sequence)

    sequence_counts = {}
    for sequence in sequences:
        sequence_counts[sequence] = sequence_counts.get(sequence, 0) + 1

    most_frequent = sorted(sequence_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return most_frequent

if __name__ == "__main__":
    fasta_file_path = "sample_files/fasta/sample.fasta"  
    result = find_most_frequent_sequences(fasta_file_path)

    print("Top 10 Most Frequent Sequences:")
    for sequence, count in result:
        print(f"{sequence}: {count} occurrences")