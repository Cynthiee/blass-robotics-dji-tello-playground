import time
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

def read_sim_key_file(filepath):
    with open(filepath, 'r') as file:
        return file.readline().strip()

def perform_takeoff(drone):
    """Handles the drone takeoff."""
    drone.takeoff()

def fly_triangle(drone, side_length):
    """Makes the drone fly in a triangular pattern."""
    # Fly to the first vertex
    drone.fly_to_xyz(side_length, 0, 0, 'cm')
    
    # Fly to the second vertex (forming a 60-degree angle)
    drone.fly_to_xyz(side_length / 2, (side_length * (3 ** 0.5)) / 2, 0, 'cm')
    
    # Fly back to the starting point (closing the triangle)
    drone.fly_to_xyz(0, 0, 0, 'cm')

    perform_landing(drone)


def measure_time():
    """Starts the timer."""
    return time.time()

def calculate_elapsed_time(start_time):
    """Calculates and returns the elapsed time since start_time."""
    end_time = time.time()
    return end_time - start_time

def print_elapsed_time(elapsed_time):
    """Prints the elapsed time."""
    print(f"Time elapsed: {elapsed_time:.2f} seconds")

def perform_landing(drone):
    """Handles the drone landing."""
    drone.land()

def main(sim_key):
    """Main function to control the drone operations."""
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        perform_takeoff(drone)
        
        start_time = measure_time()
        
        # Fly in a triangular pattern
        fly_triangle(drone, 100)  # Side length of 100 cm
        
        elapsed_time = calculate_elapsed_time(start_time)
        print_elapsed_time(elapsed_time)
        
        perform_landing(drone)

if __name__ == '__main__':
    main(sim_key)
