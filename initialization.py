import numpy as np
import calculations


def initialize_forces(masses, positions, frame):
    """Initialize forces for the first frame."""
    forces = np.zeros((len(masses), 2))
    calculations.update_forces(positions, masses, forces, frame)
    return forces


def initialize_bodies(number_of_frames):
    """Initialize masses, positions, and velocities."""
    number_of_bodies = int(input("Enter the number of bodies: "))
    masses = np.array([float(input(f"Mass of body {i + 1}: ")) for i in range(number_of_bodies)])

    positions = np.zeros((number_of_bodies, 2, number_of_frames))
    for i in range(number_of_bodies):
        positions[i][0][0] = float(input(f"Initial x-coordinate of body {i + 1}: "))
        positions[i][1][0] = float(input(f"Initial y-coordinate of body {i + 1}: "))

    velocities = np.zeros((number_of_bodies, 2, number_of_frames))
    for i in range(number_of_bodies):
        velocities[i][0][0] = float(input(f"Initial velocity in x-direction of body {i + 1}: "))
        velocities[i][1][0] = float(input(f"Initial velocity in y-direction of body {i + 1}: "))

    forces = initialize_forces(masses, positions, 0)
    return masses, positions, velocities, forces


def initialize_simulation():
    """Initialize simulation parameters."""
    time_upper_limit = float(input("Enter time upper limit (seconds): "))
    delta_t = float(input("Enter time step (seconds): "))
    if delta_t <= 0 or time_upper_limit <= delta_t:
        raise ValueError("Invalid time parameters.")

    number_of_frames = int(time_upper_limit / delta_t) + 1
    masses, positions, velocities, forces = initialize_bodies(number_of_frames)
    return time_upper_limit, masses, positions, velocities, forces, delta_t
