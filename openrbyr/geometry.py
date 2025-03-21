# geometry.py
"""
Define CT scanner geometries (fan-beam, cone-beam, parallel-beam).
"""
import numpy as np

class CTGeometry:
    def __init__(self, num_detectors, detector_spacing, source_to_detector, source_to_center):
        self.num_detectors = num_detectors
        self.detector_spacing = detector_spacing
        self.source_to_detector = source_to_detector
        self.source_to_center = source_to_center

    def get_detector_positions(self):
        """Returns the physical (x, y) positions of each detector."""
        angles = np.linspace(-np.pi / 2, np.pi / 2, self.num_detectors)
        x = self.source_to_center + self.source_to_detector * np.cos(angles)
        y = self.source_to_detector * np.sin(angles)
        return np.stack((x, y), axis=-1)

    def get_source_position(self, angle_rad):
        """Returns the (x, y) position of the X-ray source at a given angle."""
        x = self.source_to_center * np.cos(angle_rad)
        y = self.source_to_center * np.sin(angle_rad)
        return np.array([x, y])

    def describe(self):
        print("CT Geometry:")
        print(f"  Detectors: {self.num_detectors}")
        print(f"  Spacing: {self.detector_spacing} mm")
        print(f"  Source-to-Detector: {self.source_to_detector} mm")
        print(f"  Source-to-Center: {self.source_to_center} mm")

