# cli/phantom_cli.py
"""
Command-line tool to load, visualize, and optionally save CT phantom files.
"""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

from core.phantom_loader import (
    load_image_phantom,
    load_dicom_phantom,
    load_nifti_phantom,
    auto_load_phantom,
    load_phantom_batch
)

def display_phantom(image, title="Phantom"):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def save_numpy(image, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    np.save(out_path, image)
    print(f"Saved phantom as NumPy array to {out_path}.npy")

def main():
    parser = argparse.ArgumentParser(description="Load and visualize CT phantom files.")
    parser.add_argument('--input', type=str, help="Path to a single phantom file")
    parser.add_argument('--folder', type=str, help="Folder path to batch load phantoms")
    parser.add_argument('--resize', nargs=2, type=int, default=[256, 256], help="Resize to (H, W)")
    parser.add_argument('--show', action='store_true', help="Display the loaded phantom(s)")
    parser.add_argument('--save', type=str, help="Save loaded phantom(s) as .npy")
    args = parser.parse_args()

    size = tuple(args.resize)

    if args.input:
        phantom = auto_load_phantom(args.input, size=size)
        if args.show:
            display_phantom(phantom, title=os.path.basename(args.input))
        if args.save:
            filename = os.path.splitext(os.path.basename(args.input))[0]
            save_numpy(phantom, os.path.join(args.save, filename))

    elif args.folder:
        phantoms = load_phantom_batch(args.folder, size=size)
        for idx, phantom in enumerate(phantoms):
            name = f"phantom_{idx}"
            if args.show:
                display_phantom(phantom, title=name)
            if args.save:
                save_numpy(phantom, os.path.join(args.save, name))
    else:
        print("Please specify --input or --folder")

if __name__ == '__main__':
    main()

