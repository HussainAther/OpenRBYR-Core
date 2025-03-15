# example_ray_trace.py
from openrbyr.ray_simulation import RaySimulation

sim = RaySimulation(num_rays=50, detector_distance=40)
rays = sim.simulate_rays()
sim.visualize_rays(rays)

