import os
import glob
import requests

# Path to the text files
descriptionsPath = 'supplier-data/descriptions/*.txt'
descriptionsList = glob.glob(descriptionsPath)
url = 'http://35.232.233.234/fruits/'

# List to hold all product data
products = []

for description in descriptionsList:
    product_dict = {}  # Renamed to avoid using built-in name 'dict'
    
    with open(description) as d:
        lines = d.readlines()
        
        # Construct the product dictionary
        product_dict['name'] = lines[0].strip()
        product_dict['weight'] = lines[1].split()[0]  # Assuming weight is the first word
        product_dict['description'] = lines[2].strip()
        product_dict['image_name'] = os.path.splitext(os.path.basename(description))[0] + '.jpeg'
    
    # Sending POST request to the server
    try:
        response = requests.post(url, json=product_dict)  # Use json parameter for correct content type
        response.raise_for_status()  # Raise an error for bad responses
        print(f"Successfully uploaded: {product_dict['name']} - Status Code: {response.status_code}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for {product_dict['name']}: {http_err}")
    except Exception as err:
        print(f"An error occurred for {product_dict['name']}: {err}")

print("Finished uploading all products.")
print(product_dict)
