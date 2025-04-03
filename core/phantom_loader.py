# core/phantom_loader.py
"""
Load CT phantoms from image files (PNG, JPG) or medical formats (optional).
"""
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
import os

def load_image_phantom(filepath, size=(256, 256)):
    """
    Load and normalize a phantom image (PNG, JPG).

    Args:
        filepath (str): Path to the phantom image
        size (tuple): Desired output size (height, width)

    Returns:
        np.ndarray: Resized, normalized phantom in range [0, 1]
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Phantom file not found: {filepath}")

    img = imread(filepath)
    if img.ndim == 3:
        img = rgb2gray(img)
    img_resized = resize(img, size, mode='reflect', anti_aliasing=True)
    img_normalized = (img_resized - np.min(img_resized)) / (np.max(img_resized) - np.min(img_resized) + 1e-8)
    return img_normalized

# Future expansion: DICOM, NIfTI loaders
# def load_dicom_phantom(...):
# def load_nifti_phantom(...):

if __name__ == "__main__":
    phantom = load_image_phantom("../phantoms/custom_phantom.png")
    import matplotlib.pyplot as plt
    plt.imshow(phantom, cmap='gray')
    plt.title("Loaded Phantom")
    plt.axis('off')
    plt.show()

