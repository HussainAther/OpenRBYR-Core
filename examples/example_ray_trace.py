# examples/example_ray_trace.py
"""
Visualize ray paths through a phantom using Siddon's algorithm.
"""
import matplotlib.pyplot as plt
from core.geometry import CTGeometry
from core.phantoms import generate_shepp_logan
from core.ray_generator import generate_ray_pairs
from core.interpolation import siddons_algorithm
import numpy as np

# Setup
phantom = generate_shepp_logan(256)
geo = CTGeometry(
    num_angles=1,  # Single angle for clarity
    num_detectors=32,
    detector_spacing=1.0,
    source_to_center=500,
    source_to_detector=1000
)
rays = generate_ray_pairs(geo)[0]  # One angle's rays only

# Plot phantom
plt.imshow(phantom, cmap="gray", extent=[0, phantom.shape[1], phantom.shape[0], 0])
plt.title("Ray Paths over Shepp-Logan Phantom")

# Overlay rays
for src, det in rays:
    plt.plot([src[0], det[0]], [src[1], det[1]], color='red', alpha=0.4, linewidth=0.5)
    plt.scatter(*src, color='blue', s=5)  # Source point
    plt.scatter(*det, color='green', s=5)  # Detector point

plt.axis('off')
plt.tight_layout()
plt.show()
