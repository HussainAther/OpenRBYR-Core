# examples/example_custom_phantom.py
"""
Load a custom phantom from a PNG image and run full simulation pipeline.
"""
import numpy as np
import matplotlib.pyplot as plt
from imageio import imread
from skimage.transform import resize
from skimage.color import rgb2gray

from core.geometry import CTGeometry
from core.ray_generator import generate_ray_pairs
from core.projection import forward_project
from core.noise_models import add_poisson_noise
from core.filters import apply_filter, ramp_filter
from core.backprojection import backproject

# Load and preprocess custom phantom
phantom_img = imread("phantoms/custom_phantom.png")
if phantom_img.ndim == 3:
    phantom_img = rgb2gray(phantom_img)
phantom = resize(phantom_img, (256, 256), mode='reflect', anti_aliasing=True)
phantom = (phantom - phantom.min()) / (phantom.max() - phantom.min())

# CT Simulation Setup
geo = CTGeometry(num_angles=180, num_detectors=256, detector_spacing=1.0,
                 source_to_center=500, source_to_detector=1000)
rays = generate_ray_pairs(geo)

# Projection → Noise → Filter → Backproject
sinogram = forward_project(phantom, rays, phantom.shape, pixel_size=1.0)
sinogram_noisy = add_poisson_noise(sinogram, scale=1e4)
sinogram_filtered = apply_filter(sinogram_noisy, ramp_filter)
reconstruction = backproject(sinogram_filtered, rays, phantom.shape, pixel_size=1.0)

# Display Results
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(phantom, cmap='gray')
axes[0].set_title("Custom Phantom")
axes[1].imshow(sinogram_filtered, cmap='gray', aspect='auto')
axes[1].set_title("Filtered Sinogram")
axes[2].imshow(reconstruction, cmap='gray')
axes[2].set_title("Reconstruction")

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()

