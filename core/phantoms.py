# core/phantoms.py
"""
Generate 2D synthetic CT phantoms (Shepp-Logan, synthetic breast tissue).
"""
import numpy as np
from skimage.data import shepp_logan_phantom
from skimage.transform import resize

def generate_shepp_logan(size=256):
    """Generates a 2D Shepp-Logan phantom scaled to the specified size."""
    phantom = shepp_logan_phantom()
    phantom_resized = resize(phantom, (size, size), mode='reflect', anti_aliasing=True)
    return phantom_resized

def generate_breast_tissue(size=256):
    """Generates a simple synthetic breast tissue phantom with embedded circular tumors."""
    phantom = np.ones((size, size)) * 0.1  # soft tissue background

    # Synthetic tumors
    rr, cc = np.ogrid[:size, :size]
    tumor1 = (rr - size // 3)**2 + (cc - size // 3)**2 < (size // 10)**2
    tumor2 = (rr - 2 * size // 3)**2 + (cc - 2 * size // 3)**2 < (size // 12)**2

    phantom[tumor1] = 0.8  # High density mass
    phantom[tumor2] = 0.6  # Moderate density mass

    return phantom

def normalize(phantom):
    """Normalize phantom values to range [0, 1]."""
    return (phantom - np.min(phantom)) / (np.max(phantom) - np.min(phantom) + 1e-8)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    phantom1 = generate_shepp_logan()
    phantom2 = generate_breast_tissue()

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(phantom1, cmap='gray')
    axes[0].set_title("Shepp-Logan Phantom")
    axes[1].imshow(phantom2, cmap='gray')
    axes[1].set_title("Synthetic Breast Phantom")
    for ax in axes:
        ax.axis('off')
    plt.tight_layout()
    plt.show()

