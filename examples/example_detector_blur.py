# examples/example_detector_blur.py
"""
Demonstrates the effect of detector blur on sinograms.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

from core.phantoms import generate_shepp_logan
from core.geometry import CTGeometry
from core.ray_generator import generate_ray_pairs
from core.projection import forward_project

# Setup
phantom = generate_shepp_logan(256)
geo = CTGeometry(180, 180, 1.0, 500, 1000)
rays = generate_ray_pairs(geo)

# Forward projection (ideal detector)
sinogram_clean = forward_project(phantom, rays, phantom.shape, pixel_size=1.0)

# Simulate detector blur using Gaussian filter
sinogram_blurred = gaussian_filter(sinogram_clean, sigma=(0, 2))  # Blur only across detectors

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(phantom, cmap='gray')
axes[0].set_title("Phantom")
axes[1].imshow(sinogram_clean, cmap='gray', aspect='auto')
axes[1].set_title("Ideal Sinogram")
axes[2].imshow(sinogram_blurred, cmap='gray', aspect='auto')
axes[2].set_title("Blurred Sinogram (Detector)")

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()

