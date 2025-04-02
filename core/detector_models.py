# core/detector_models.py
"""
Simulate CT detector imperfections: blur, saturation, and noise.
"""
import numpy as np
from scipy.ndimage import gaussian_filter

def apply_detector_blur(sinogram, sigma=2):
    """
    Applies Gaussian blur across detectors to simulate detector PSF (point spread function).

    Args:
        sinogram (np.ndarray): Raw sinogram [angles x detectors]
        sigma (float): Standard deviation of Gaussian blur (in detector pixels)

    Returns:
        np.ndarray: Blurred sinogram
    """
    return gaussian_filter(sinogram, sigma=(0, sigma))

def apply_saturation(sinogram, max_value=5.0):
    """
    Simulate detector saturation by clipping high attenuation values.

    Args:
        sinogram (np.ndarray): Input sinogram
        max_value (float): Maximum log attenuation before saturation

    Returns:
        np.ndarray: Saturated sinogram
    """
    return np.clip(sinogram, a_min=0, a_max=max_value)

def apply_detector_gain(sinogram, gain_map):
    """
    Apply per-detector gain variation.

    Args:
        sinogram (np.ndarray): Input sinogram
        gain_map (np.ndarray): 1D array with detector multipliers [detectors]

    Returns:
        np.ndarray: Gain-modified sinogram
    """
    return sinogram * gain_map[np.newaxis, :]

if __name__ == "__main__":
    print("Detector models module loaded.")

