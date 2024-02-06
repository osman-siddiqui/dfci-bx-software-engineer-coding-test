import pandas as pd

def calculate_gc_bin(gc_value):
    try:
        return int(float(gc_value) * 100 // 10) * 10
    except ValueError:
        return None

def calculate_mean_coverage_by_gc(data_frame):
    data_frame['gc_bin'] = data_frame['%gc'].apply(calculate_gc_bin)
    data_frame['mean_coverage'] = pd.to_numeric(data_frame['mean_coverage'], errors='coerce')
    return data_frame.groupby('gc_bin')['mean_coverage'].mean().reset_index()

def read_input_file(input_file):
    try:
        return pd.read_csv(input_file, sep='\t', usecols=['%gc', 'mean_coverage'], dtype={'%gc': float, 'mean_coverage': float})
    except pd.errors.EmptyDataError:
        return pd.DataFrame()

def save_results(grouped_data, output_file):
    grouped_data.to_csv(output_file, sep='\t', index=False)
    print(f"Results saved to {output_file}")

def main(input_file, output_file):
    try:
        df = read_input_file(input_file)
        if not df.empty:
            grouped_data = calculate_mean_coverage_by_gc(df)
            save_results(grouped_data, output_file)
        else:
            print("Input file is empty or has invalid data.")

    except Exception as e:
        print(f"Error processing input file: {e}")
        print("Please check the file for formatting issues.")

if __name__ == "__main__":
    input_file_path = "Example.hs_intervals.txt"
    output_file_path = "mean_coverage_by_gc_bins.txt"
    main(input_file_path, output_file_path)