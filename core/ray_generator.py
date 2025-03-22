# core/ray_generator.py
"""
Generate ray paths between source and detector positions for each angle.
"""
import numpy as np
from core.geometry import CTGeometry


def generate_ray_pairs(geometry: CTGeometry):
    """
    Generate all source-detector ray pairs for each projection angle.

    Args:
        geometry (CTGeometry): CT geometry configuration

    Returns:
        List[List[Tuple[source: np.ndarray, detector: np.ndarray]]]
        A list of rays per angle, each ray as (source, detector) tuple
    """
    all_rays = []
    angles = geometry.get_angles()

    for angle in angles:
        source = geometry.get_source_position(angle)
        detectors = geometry.get_detector_positions(angle)
        rays = [(source, det) for det in detectors]
        all_rays.append(rays)

    return all_rays


if __name__ == "__main__":
    geo = CTGeometry(
        num_angles=180,
        num_detectors=128,
        detector_spacing=1.0,
        source_to_center=500,
        source_to_detector=1000
    )
    ray_pairs = generate_ray_pairs(geo)
    print(f"Generated rays for {len(ray_pairs)} angles")
    print(f"Rays per angle: {len(ray_pairs[0])}")
    print("Example ray (source → detector):", ray_pairs[0][0])

