import numpy as np
import os
import json

def save_array_to_file(array, filename):
    np.save(filename, array)
    print(f"Array saved to {filename}")

def load_array_from_file(filename):
    if os.path.exists(filename):
        return np.load(filename)
    else:
        print(f"File {filename} not found.")
        return None

def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"JSON data saved to {filename}")

def load_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        print(f"File {filename} not found.")
        return None

