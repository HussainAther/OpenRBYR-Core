# api_server.py

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from openrbyr.ray_simulation import RaySimulation
from openrbyr.monte_carlo import MonteCarloSimulation
from openrbyr.reconstruction import MARTReconstruction

app = FastAPI()

# Define request models
class RaySimulationRequest(BaseModel):
    num_rays: int
    detector_distance: float

class MonteCarloRequest(BaseModel):
    num_particles: int
    detector_distance: float

class ReconstructionRequest(BaseModel):
    projections: list
    num_iterations: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the OpenRBYR API!"}

@app.post("/simulate_rays")
def simulate_rays(request: RaySimulationRequest):
    sim = RaySimulation(request.num_rays, request.detector_distance)
    rays = sim.simulate_rays()
    return {"rays": rays}

@app.post("/monte_carlo")
def run_monte_carlo(request: MonteCarloRequest):
    mc_sim = MonteCarloSimulation(request.num_particles, request.detector_distance)
    interactions = mc_sim.run_simulation()
    results = mc_sim.analyze_results(interactions)
    return {"results": results}

@app.post("/reconstruct")
def reconstruct_image(request: ReconstructionRequest):
    recon = MARTReconstruction(request.num_iterations)
    reconstructed_image = recon.reconstruct(np.array(request.projections))
    return {"reconstructed_image": reconstructed_image.tolist()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

