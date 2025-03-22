# core/geometry.py
"""
Defines CT scanner geometry for 2D fan-beam simulations.
"""
import numpy as np

class CTGeometry:
    def __init__(self, num_angles, num_detectors, detector_spacing, source_to_center, source_to_detector):
        self.num_angles = num_angles
        self.num_detectors = num_detectors
        self.detector_spacing = detector_spacing
        self.source_to_center = source_to_center
        self.source_to_detector = source_to_detector

    def get_angles(self):
        """Returns an array of evenly spaced projection angles (in radians)."""
        return np.linspace(0, 2 * np.pi, self.num_angles, endpoint=False)

    def get_source_position(self, angle_rad):
        """Returns the (x, y) position of the X-ray source at a given angle."""
        x = self.source_to_center * np.cos(angle_rad)
        y = self.source_to_center * np.sin(angle_rad)
        return np.array([x, y])

    def get_detector_positions(self, angle_rad):
        """
        Returns the (x, y) positions of each detector at a given projection angle.
        Detectors are assumed to lie on a circular arc centered at the rotation center.
        """
        arc = np.linspace(-self.num_detectors // 2, self.num_detectors // 2, self.num_detectors)
        angle_offsets = arc * self.detector_spacing / self.source_to_detector

        det_angles = angle_rad + np.pi - angle_offsets
        x = self.source_to_center * np.cos(angle_rad) + self.source_to_detector * np.cos(det_angles)
        y = self.source_to_center * np.sin(angle_rad) + self.source_to_detector * np.sin(det_angles)
        return np.stack((x, y), axis=-1)

    def describe(self):
        print("CT Geometry Config:")
        print(f"  Projections: {self.num_angles}")
        print(f"  Detectors: {self.num_detectors}")
        print(f"  Detector Spacing: {self.detector_spacing} mm")
        print(f"  Source-to-Center: {self.source_to_center} mm")
        print(f"  Source-to-Detector: {self.source_to_detector} mm")

