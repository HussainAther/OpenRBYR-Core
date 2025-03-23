# core/projection.py
"""
Forward projection (A · x) using Siddon's algorithm and ray tracing.
"""
import numpy as np
from core.interpolation import siddons_algorithm


def forward_project(phantom, rays, grid_shape, pixel_size=1.0):
    """
    Computes the sinogram for a given phantom and set of rays using line integrals.

    Args:
        phantom (np.ndarray): 2D image (phantom)
        rays (List[List[Tuple[np.ndarray, np.ndarray]]]): List of rays per angle
        grid_shape (Tuple[int, int]): Shape of the image grid
        pixel_size (float): Physical size of each pixel

    Returns:
        np.ndarray: 2D sinogram (angles x detectors)
    """
    sinogram = []
    for angle_rays in rays:
        projection = []
        for source, detector in angle_rays:
            ray = siddons_algorithm(source, detector, grid_shape, pixel_size)
            value = sum(phantom[i, j] * length for i, j, length in ray)
            projection.append(value)
        sinogram.append(projection)
    return np.array(sinogram)


if __name__ == "__main__":
    # Example test usage (not full pipeline)
    phantom = np.ones((128, 128))
    from core.geometry import CTGeometry
    from core.ray_generator import generate_ray_pairs

    geometry = CTGeometry(num_angles=90, num_detectors=128, detector_spacing=1.0,
                          source_to_center=500, source_to_detector=1000)
    rays = generate_ray_pairs(geometry)

    sino = forward_project(phantom, rays, phantom.shape, pixel_size=1.0)
    print("Sinogram shape:", sino.shape)

