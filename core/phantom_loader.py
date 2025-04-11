# core/phantom_loader.py
"""
Load CT phantoms from image files (PNG, JPG), DICOM, or NIfTI formats.
"""
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
import os

try:
    import pydicom
    from pydicom.pixel_data_handlers.util import apply_voi_lut
except ImportError:
    pydicom = None

try:
    import nibabel as nib
except ImportError:
    nib = None

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

def load_dicom_phantom(filepath, size=(256, 256)):
    """
    Load and normalize a single-slice DICOM image.

    Args:
        filepath (str): Path to DICOM file
        size (tuple): Desired output size

    Returns:
        np.ndarray: 2D normalized image
    """
    if pydicom is None:
        raise ImportError("pydicom is not installed. Please install it to use DICOM support.")
    
    ds = pydicom.dcmread(filepath)
    img = apply_voi_lut(ds.pixel_array, ds)
    img = img.astype(np.float32)
    img_resized = resize(img, size, mode='reflect', anti_aliasing=True)
    img_normalized = (img_resized - img_resized.min()) / (img_resized.max() - img_resized.min() + 1e-8)
    return img_normalized

def load_nifti_phantom(filepath, size=(256, 256)):
    """
    Load and normalize a single-slice NIfTI image.

    Args:
        filepath (str): Path to NIfTI (.nii or .nii.gz)
        size (tuple): Output size

    Returns:
        np.ndarray: 2D normalized slice
    """
    if nib is None:
        raise ImportError("nibabel is not installed. Please install it to use NIfTI support.")

    img = nib.load(filepath).get_fdata()
    slice_2d = img[:, :, img.shape[2] // 2]  # take middle slice
    img_resized = resize(slice_2d, size, mode='reflect', anti_aliasing=True)
    img_normalized = (img_resized - img_resized.min()) / (img_resized.max() - img_resized.min() + 1e-8)
    return img_normalized

if __name__ == "__main__":
    # Image example
    phantom = load_image_phantom("../phantoms/custom_phantom.png")

    # DICOM example (uncomment to use)
    # phantom = load_dicom_phantom("../phantoms/sample.dcm")

    # NIfTI example (uncomment to use)
    # phantom = load_nifti_phantom("../phantoms/sample.nii.gz")

    import matplotlib.pyplot as plt
    plt.imshow(phantom, cmap='gray')
    plt.title("Loaded Phantom")
    plt.axis('off')
    plt.show()

