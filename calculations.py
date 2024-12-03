import numpy as np
import math
from scipy.constants import G


def calculate_force(mass1, mass2, position1, position2):
    """Calculate the gravitational force between two bodies."""
    deltax = position2[0] - position1[0]
    deltay = position2[1] - position1[1]
    distance_squared = deltax**2 + deltay**2

    if distance_squared == 0:
        raise ValueError("Collision detected: Two bodies are at the same position.")

    force_magnitude = (G * mass1 * mass2) / distance_squared
    angle = math.atan2(deltay, deltax)
    force_x = force_magnitude * math.cos(angle)
    force_y = force_magnitude * math.sin(angle)
    return np.array([force_x, force_y])


def update_forces(positions, masses, forces, frame):
    """Update forces acting on all bodies."""
    forces.fill(0)  # Reset forces
    for i in range(len(masses)):
        for j in range(i + 1, len(masses)):
            force = calculate_force(masses[i], masses[j],
                                    positions[i][:, frame],
                                    positions[j][:, frame])
            forces[i] += force
            forces[j] -= force  # Newton's Third Law


def update_velocities(masses, velocities, forces, time_step, frame):
    """Update velocities based on current forces."""
    for i in range(len(velocities)):
        acceleration = forces[i] / masses[i]
        velocities[i][:, frame] = velocities[i][:, frame - 1] + acceleration * time_step


def update_positions(positions, velocities, frame, time_step):
    """Update positions based on current velocities."""
    for i in range(len(positions)):
        positions[i][:, frame] = positions[i][:, frame - 1] + velocities[i][:, frame] * time_step


def update_frame(masses, positions, velocities, forces, frame, time_step):
    """Update positions, velocities, and forces for a single frame."""
    update_forces(positions, masses, forces, frame - 1)
    update_velocities(masses, velocities, forces, time_step, frame)
    update_positions(positions, velocities, frame, time_step)
