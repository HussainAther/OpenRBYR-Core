# core/filters.py
"""
CT reconstruction filters for Filtered Backprojection (FBP):
Includes Ram-Lak, Shepp-Logan, Hamming filters in the frequency domain.
"""
import numpy as np
import scipy.fftpack as fft

def ramp_filter(size):
    """
    Generate a Ram-Lak ramp filter.
    """
    freqs = np.fft.fftfreq(size).reshape(-1, 1)
    filter_vals = 2 * np.abs(freqs)
    return filter_vals

def shepp_logan_filter(size):
    freqs = np.fft.fftfreq(size).reshape(-1, 1)
    filter_vals = 2 * np.abs(freqs) * np.sinc(freqs)
    return filter_vals

def hamming_filter(size):
    freqs = np.fft.fftfreq(size).reshape(-1, 1)
    ramp = 2 * np.abs(freqs)
    hamming_window = 0.54 + 0.46 * np.cos(np.pi * freqs / np.max(freqs))
    return ramp * hamming_window

def apply_filter(sinogram, filter_func):
    """
    Apply the given frequency filter to the sinogram.

    Args:
        sinogram (np.ndarray): [angles x detectors]
        filter_func (function): one of the filters above

    Returns:
        np.ndarray: Filtered sinogram
    """
    filtered = np.zeros_like(sinogram)
    n_angles, n_detectors = sinogram.shape
    filt = filter_func(n_detectors)

    for i in range(n_angles):
        proj_fft = fft.fft(sinogram[i])
        proj_fft *= filt[:, 0]  # Apply filter
        filtered[i] = np.real(fft.ifft(proj_fft))

    return filtered

if __name__ == "__main__":
    print("CT reconstruction filters module ready.")

