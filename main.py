import calculations
import initialization
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initialize parameters
time_upper_limit, masses, positions, velocities, forces, delta_t = initialization.initialize_simulation()
number_of_frames = int(time_upper_limit / delta_t) + 1

# Run simulation
for frame in range(1, number_of_frames):
    calculations.update_frame(masses, positions, velocities, forces, frame, delta_t)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate time points
time_points = np.linspace(0, time_upper_limit, number_of_frames)

# Plot trajectories in 3D
for i in range(len(masses)):
    ax.plot(
        positions[i][0, :],  # X-axis: x-coordinates
        positions[i][1, :],  # Y-axis: y-coordinates
        time_points,         # Z-axis: time
        label=f"Body {i + 1} Mass:{masses[i]}"
    )

# Add labels and title
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_zlabel("Time (seconds)")
ax.set_title("Trajectories of Bodies Over Time")
ax.legend()
plt.show()

figure, axes =plt.subplots(len(masses), 4, figsize=(15, 5))
a=['x','y']
for i in range(len(masses)):
    for j in range(2):
        axes[i][j].set_title(f"position in {a[j]} axis with respect to time \nBODY: {i+1}")
        axes[i][j].plot(time_points, positions[i][j,:])
        axes[i][j].set_xlabel("time")
        axes[i][j].set_ylabel(f"{a[j]} Position")
        axes[i][j+2].set_title(f"velocity in {a[j]} axis with respect to time \nBODY: {i+1}")
        axes[i][j+2].plot(time_points, velocities[i][j,:])
        axes[i][j+2].set_xlabel("time")
        axes[i][j+2].set_ylabel(f"{a[j]} Velocity")

plt.tight_layout()
plt.show()