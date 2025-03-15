import numpy as np
import matplotlib.pyplot as plt

class RaySimulation:
    def __init__(self, num_rays=100, detector_distance=50):
        self.num_rays = num_rays
        self.detector_distance = detector_distance

    def simulate_rays(self):
        angles = np.linspace(-np.pi / 4, np.pi / 4, self.num_rays)
        rays = [(np.cos(a) * self.detector_distance, np.sin(a) * self.detector_distance) for a in angles]
        return rays

    def visualize_rays(self, rays):
        plt.figure(figsize=(6, 6))
        for x, y in rays:
            plt.plot([0, x], [0, y], 'r-')
        plt.xlim(-self.detector_distance, self.detector_distance)
        plt.ylim(-self.detector_distance, self.detector_distance)
        plt.xlabel("X-ray Beam Path")
        plt.ylabel("Detector Position")
        plt.title("Ray Simulation")
        plt.show()
