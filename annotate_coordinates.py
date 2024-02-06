def load_annotations(annotations_file):
    annotations = []
    with open(annotations_file, "r") as file:
        for line in file:
            if not line.startswith("#"):
                parts = line.strip().split("\t")
                if len(parts) == 9:
                    annotation = {
                        "chromosome": parts[0],
                        "start": int(parts[3]),
                        "end": int(parts[4]),
                        "gene_name": parts[8].split(";")[0].split(" ")[1],
                    }
                    annotations.append(annotation)
    return annotations

def lookup_annotation(chromosome, start, end, annotations):
    return [ann["gene_name"] for ann in annotations if
            ann["chromosome"] == chromosome and ann["end"] >= start and ann["start"] <= end]

def annotate_coordinates(coordinates_file, annotations, output_file):
    with open(coordinates_file, "r") as input_file, open(output_file, "w") as output:
        for line in input_file:
            if not line.startswith("#"):
                parts = line.strip().split("\t")
                if len(parts) >= 2:
                    chromosome = parts[0]
                    start = end = int(parts[1])
                    if len(parts) == 3:
                        end = int(parts[2])

                    overlapping_genes = lookup_annotation(chromosome, start, end, annotations)
                    output.write(f"{chromosome}\t{start}\t{end}\t{';'.join(overlapping_genes)}\n")
                else:
                    print(f"Skipping line: {line.strip()}. Expected at least 2 values, found {len(parts)}")

if __name__ == "__main__":
    coordinates_file_path = "sample_files/annotate/coordinates_to_annotate.txt"
    annotations_file_path = "sample_files/gtf/hg19_annotations.gtf"
    output_file_path = "annotated_output.txt"

    annotations = load_annotations(annotations_file_path)
    annotate_coordinates(coordinates_file_path, annotations, output_file_path)