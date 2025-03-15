import numpy as np
import matplotlib.pyplot as plt

class MARTReconstruction:
    def __init__(self, num_iterations=10):
        self.num_iterations = num_iterations

    def reconstruct(self, projections):
        reconstructed_image = np.ones_like(projections)
        for _ in range(self.num_iterations):
            reconstructed_image *= projections / (np.sum(reconstructed_image, axis=0) + 1e-8)
        return reconstructed_image

    def visualize_reconstruction(self, image):
        plt.imshow(image, cmap='gray')
        plt.title("Reconstructed Image")
        plt.colorbar()
        plt.show()
