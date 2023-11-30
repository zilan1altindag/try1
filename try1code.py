import itertools
import requests

def try_combination(combination):
    # Fill in the actual URL here
    base_url = "http://10.0.0.6/ctf_deploy/aclive/ddjS7HkE9M/A.php"
    
    # Map parameters to their values in the combination
    params = {param: str(value).lower() for param, value in zip(parameters, combination)}
    
    # Send a GET request to the server with the current combination
    response = requests.get(base_url, params=params)
    
    # Print debug information
    print(f"Combination: {combination}, Status Code: {response.status_code}, Result: {response.text}")
    
    return response.text

# List of parameters to be tested
parameters = ["OSA","OSB","OSC","HSA","HSB","HSD"]

# Generate all possible combinations of True and False for the parameters
combinations = list(itertools.product([True, False], repeat=len(parameters)))

# Iterate through all combinations and test them
for combination in combinations:
    result = try_combination(combination)
