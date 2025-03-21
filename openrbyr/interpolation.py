# interpolation.py
"""
Ray-pixel interpolation using Siddon's algorithm for CT line integration.
"""
import numpy as np

def siddons_algorithm(start, end, grid_shape, pixel_size):
    """
    Siddon's algorithm for computing intersection lengths of a ray through a 2D grid.

    Args:
        start (tuple): (x0, y0) coordinates of the ray source
        end (tuple): (x1, y1) coordinates of the detector
        grid_shape (tuple): (num_rows, num_cols)
        pixel_size (float): physical size of each pixel

    Returns:
        list of tuples: [(i, j, length), ...] where (i, j) is the pixel and length is the distance
    """
    x0, y0 = start
    x1, y1 = end
    nx, ny = grid_shape

    dx = x1 - x0
    dy = y1 - y0
    L = np.sqrt(dx**2 + dy**2)
    
    # Normalize direction
    dx /= L
    dy /= L

    # Grid setup
    i0 = int(x0 / pixel_size)
    j0 = int(y0 / pixel_size)
    i1 = int(x1 / pixel_size)
    j1 = int(y1 / pixel_size)

    intersected = []

    N = int(max(abs(i1 - i0), abs(j1 - j0)) * 1.5)  # oversample
    for step in np.linspace(0, L, N):
        x = x0 + dx * step
        y = y0 + dy * step
        i = int(x / pixel_size)
        j = int(y / pixel_size)
        if 0 <= i < nx and 0 <= j < ny:
            intersected.append((i, j))

    # Count lengths
    from collections import Counter
    counts = Counter(intersected)
    results = [(i, j, c * L / N) for (i, j), c in counts.items()]
    return results

if __name__ == "__main__":
    # Example usage
    src = (10.0, 10.0)
    det = (80.0, 80.0)
    pixels = siddons_algorithm(src, det, grid_shape=(128, 128), pixel_size=1.0)
    print(f"Ray intersects {len(pixels)} pixels")

