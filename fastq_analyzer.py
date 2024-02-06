import os
from Bio import SeqIO

def count_long_sequences(file_path):
    try:
        with open(file_path, "r") as handle:
            records = list(SeqIO.parse(handle, "fastq"))

        total_sequences = len(records)
        long_sequences = sum(1 for record in records if len(record.seq) > 30)

        if total_sequences > 0:
            percent_long_sequences = (long_sequences / total_sequences) * 100
            return f"{file_path}: {percent_long_sequences:.2f}% of sequences > 30 nucleotides"
        else:
            return f"{file_path}: No sequences found"

    except Exception as e:
        return f"Error processing {file_path}: {e}"

def analyze_fastq_files(directory):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".fastq"):
                file_path = os.path.join(root, file)
                result = count_long_sequences(file_path)
                results.append(result)
    
    return results

if __name__ == "__main__":
    directory_path = "sample_files/fastq"
    results = analyze_fastq_files(directory_path)

    for result in results:
        print(result)