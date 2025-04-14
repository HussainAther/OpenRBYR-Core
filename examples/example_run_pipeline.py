# examples/example_run_pipeline.py
"""
Run a full CT simulation pipeline from phantom to reconstruction.
Includes options for noise, filtering, and visualization.
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
from core.phantom_loader import auto_load_phantom
from core.geometry import CTGeometry
from core.ray_generator import generate_ray_pairs
from core.projection import forward_project
from core.noise_models import add_poisson_noise, add_gaussian_noise
from core.filters import apply_filter, ramp_filter
from core.backprojection import backproject


def plot_pipeline(phantom, sinogram, filtered, recon):
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    axes[0].imshow(phantom, cmap='gray')
    axes[0].set_title("Original Phantom")
    axes[1].imshow(sinogram, cmap='gray', aspect='auto')
    axes[1].set_title("Noisy Sinogram")
    axes[2].imshow(filtered, cmap='gray', aspect='auto')
    axes[2].set_title("Filtered Sinogram")
    axes[3].imshow(recon, cmap='gray')
    axes[3].set_title("Reconstruction")
    for ax in axes:
        ax.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Run a full CT simulation pipeline.")
    parser.add_argument('--input', type=str, required=True, help="Input phantom file (.png, .dcm, .nii.gz)")
    parser.add_argument('--size', nargs=2, type=int, default=[256, 256], help="Resize phantom to H W")
    parser.add_argument('--noise', type=str, choices=['poisson', 'gaussian', 'none'], default='poisson')
    parser.add_argument('--output', type=str, help="Save reconstruction as .npy file")
    parser.add_argument('--show', action='store_true', help="Visualize pipeline results")
    args = parser.parse_args()

    size = tuple(args.size)

    # Load phantom
    phantom = auto_load_phantom(args.input, size=size)

    # Setup geometry & rays
    geo = CTGeometry(num_angles=180, num_detectors=256, detector_spacing=1.0,
                     source_to_center=500, source_to_detector=1000)
    rays = generate_ray_pairs(geo)

    # Forward projection
    sinogram = forward_project(phantom, rays, phantom.shape, pixel_size=1.0)

    # Add noise
    if args.noise == 'poisson':
        noisy_sinogram = add_poisson_noise(sinogram)
    elif args.noise == 'gaussian':
        noisy_sinogram = add_gaussian_noise(sinogram, std=0.01)
    else:
        noisy_sinogram = sinogram

    # Filter and reconstruct
    filtered = apply_filter(noisy_sinogram, ramp_filter)
    recon = backproject(filtered, rays, phantom.shape, pixel_size=1.0)

    # Save result if needed
    if args.output:
        np.save(args.output, recon)
        print(f"Reconstruction saved to {args.output}.npy")

    # Visualize
    if args.show:
        plot_pipeline(phantom, noisy_sinogram, filtered, recon)


if __name__ == "__main__":
    main()

