# example_reconstruction.py
import numpy as np
from openrbyr.reconstruction import MARTReconstruction

fake_projections = np.random.rand(50, 50)
reconstructor = MARTReconstruction(num_iterations=5)
reconstructed_image = reconstructor.reconstruct(fake_projections)
reconstructor.visualize_reconstruction(reconstructed_image)

