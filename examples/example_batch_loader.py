# examples/example_batch_loader.py
"""
Load a batch of phantom files from a folder, display them, and save as .npy files.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from core.phantom_loader import load_phantom_batch

# Parameters
input_folder = "../phantoms"
output_folder = "../outputs"
resize_shape = (256, 256)

# Load all phantoms in the folder
phantoms = load_phantom_batch(input_folder, size=resize_shape)
print(f"Loaded {len(phantoms)} phantoms from '{input_folder}'")

# Preview all phantoms in a grid
cols = 5
rows = int(np.ceil(len(phantoms) / cols))
fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
for i, ax in enumerate(axes.flat):
    if i < len(phantoms):
        ax.imshow(phantoms[i], cmap='gray')
        ax.set_title(f"Phantom {i}")
        ax.axis('off')
    else:
        ax.axis('off')
plt.tight_layout()
plt.show()

# Save each phantom as a NumPy file
os.makedirs(output_folder, exist_ok=True)
for i, phantom in enumerate(phantoms):
    filename = os.path.join(output_folder, f"phantom_{i}.npy")
    np.save(filename, phantom)
    print(f"Saved: {filename}")

