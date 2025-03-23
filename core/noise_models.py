# core/noise_models.py
"""
Noise models for CT sinograms: Poisson and Gaussian noise.
"""
import numpy as np

def add_poisson_noise(sinogram, scale=1e4):
    """
    Apply Poisson noise to simulate photon counting statistics.

    Args:
        sinogram (np.ndarray): Clean sinogram values (log attenuations)
        scale (float): Incident photon count (higher means less noise)

    Returns:
        np.ndarray: Noisy sinogram
    """
    photons = scale * np.exp(-sinogram)
    noisy = np.random.poisson(photons)
    noisy = -np.log(noisy / scale + 1e-8)
    return noisy

def add_gaussian_noise(sinogram, mean=0.0, std=0.01):
    """
    Apply Gaussian noise to simulate electronic or readout noise.

    Args:
        sinogram (np.ndarray): Clean sinogram values
        mean (float): Mean of Gaussian noise
        std (float): Standard deviation of Gaussian noise

    Returns:
        np.ndarray: Noisy sinogram
    """
    noise = np.random.normal(mean, std, size=sinogram.shape)
    return sinogram + noise

if __name__ == "__main__":
    print("Noise models module ready.")

