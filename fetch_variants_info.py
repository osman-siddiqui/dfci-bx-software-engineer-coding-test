import requests
import json

def fetch_variant_info(species, variant_id):
    url = f'https://rest.ensembl.org/variation/{species}/{variant_id}'

    # Set headers to get JSON response
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        variant_info = response.json()
        return variant_info
    else:
        print(f"Error fetching variant info. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

def main():
    species = 'human'  # Specify the species (e.g., 'human')
    # Read variant IDs from a file
    with open('variant_ids.txt', 'r') as file:
        variant_ids = [line.strip() for line in file]

    # Fetch information for each variant ID
    for variant_id in variant_ids:
        variant_info = fetch_variant_info(species, variant_id)

        if variant_info:
            # Print or process the retrieved variant information as needed
            print(f"Variant ID: {variant_id}")
            print(json.dumps(variant_info, indent=2))

if __name__ == "__main__":
    main()
