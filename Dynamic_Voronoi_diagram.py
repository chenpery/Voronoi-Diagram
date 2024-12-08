import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib

# Set the backend for interactive mode
matplotlib.use('TkAgg')  # Ensure you're using a stable backend

# Global variables
obstacle_points = [(2, 2), (8, 2), (5, 7), (3, 5)]  # Non-collinear points
grid_size = (10, 10)  # Grid size


# Function to handle Voronoi diagram creation
def create_voronoi_diagram(obstacles, ax):
    ax.clear()  # Clear the axes to avoid overlapping drawings
    # Redraw the grid
    ax.set_xlim(0, grid_size[0])
    ax.set_ylim(0, grid_size[1])
    ax.set_xticks(np.arange(0, grid_size[0] + 1, 0.5))  # Finer grid (0.5 spacing)
    ax.set_yticks(np.arange(0, grid_size[1] + 1, 0.5))  # Finer grid
    ax.grid(True)

    # Plot the obstacle points
    for point in obstacles:
        ax.plot(point[0], point[1], 'ks', markersize=10)  # Black squares for obstacles

    # Draw the Voronoi diagram if enough points are available
    if len(obstacles) > 3:  # At least 4 points are needed for Voronoi in 2D
        vor = Voronoi(obstacles)
        voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue')
    else:
        print("Need at least four points for Voronoi diagram")


# Function to handle click events
def on_click(event, ax):
    global obstacle_points
    if event.xdata is not None and event.ydata is not None:
        x, y = round(event.xdata, 1), round(event.ydata, 1)

        # Check if the clicked point is already an obstacle
        point = (x, y)

        if point in obstacle_points:
            # Remove obstacle if point is already in the list
            obstacle_points.remove(point)
            print(f"Removed obstacle at {point}")
        else:
            # Add obstacle if point is not in the list
            obstacle_points.append(point)
            print(f"Added obstacle at {point}")

        # Redraw the grid and Voronoi diagram
        create_voronoi_diagram(obstacle_points, ax)
        plt.draw()  # Refresh the figure


# Main function
def main():
    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, grid_size[0])
    ax.set_ylim(0, grid_size[1])
    ax.set_xticks(np.arange(0, grid_size[0] + 1, 0.5))  # Finer grid (0.5 spacing)
    ax.set_yticks(np.arange(0, grid_size[1] + 1, 0.5))  # Finer grid
    ax.grid(True)

    # Connect the click event to the handler
    cid = fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, ax))

    # Draw the initial grid and Voronoi diagram
    create_voronoi_diagram(obstacle_points, ax)

    plt.show()  # Keep the window open


# Run the main function
if __name__ == "__main__":
    main()
