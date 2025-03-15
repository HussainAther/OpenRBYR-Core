# example_monte_carlo.py
from openrbyr.monte_carlo import MonteCarloSimulation

mc_sim = MonteCarloSimulation(num_particles=5000, detector_distance=40)
interactions = mc_sim.run_simulation()
results = mc_sim.analyze_results(interactions)
print("Monte Carlo Simulation Results:", results)

