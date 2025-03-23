# core/backprojection.py
"""
Naive backprojection of a sinogram to reconstruct a 2D CT image.
"""
import numpy as np
from core.interpolation import siddons_algorithm

def backproject(sinogram, rays, image_shape, pixel_size=1.0):
    """
    Perform naive (unfiltered) backprojection to reconstruct an image.

    Args:
        sinogram (np.ndarray): 2D array of shape [angles x detectors]
        rays (List[List[Tuple[np.ndarray, np.ndarray]]]): List of rays per angle
        image_shape (Tuple[int, int]): Output image size (H, W)
        pixel_size (float): Physical size of each voxel

    Returns:
        np.ndarray: 2D reconstructed image
    """
    reconstruction = np.zeros(image_shape)
    weight_map = np.zeros(image_shape)

    for angle_idx, angle_rays in enumerate(rays):
        for det_idx, (source, detector) in enumerate(angle_rays):
            projection_value = sinogram[angle_idx, det_idx]
            intersected = siddons_algorithm(source, detector, image_shape, pixel_size)
            for i, j, length in intersected:
                reconstruction[i, j] += projection_value * length
                weight_map[i, j] += length

    # Normalize
    with np.errstate(divide='ignore', invalid='ignore'):
        reconstruction = np.where(weight_map > 0, reconstruction / weight_map, 0)

    return reconstruction

if __name__ == "__main__":
    print("Backprojection module loaded.")

