import time
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

sim_key = '3161934b-eb8a-423b-b6be-13c1022f1494'

def perform_takeoff(drone):
    """Handles the drone takeoff."""
    drone.takeoff()

def fly_square_pattern(drone, distance):
    """Flies the drone in a square pattern based on the given distance."""
    coordinates = [
        (100, 100, 0),
        (100, -100, 0),
        (-100, -100, 0),
        (-100, 100, 0)
    ]
    
    for x, y, z in coordinates:
        drone.fly_to_xyz(x, y, z, 'cm')

def measure_time():
    """Starts the timer."""
    return time.time()

def calculate_elapsed_time(start_time):
    """Calculates and returns the elapsed time since start_time."""
    end_time = time.time()
    return end_time - start_time

def perform_landing(drone):
    """Handles the drone landing."""
    drone.land()

def main(sim_key):
    """Main function to control the drone operations."""
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        perform_takeoff(drone)
        
        start_time = measure_time()
        fly_square_pattern(drone, 100)
        
        elapsed_time = calculate_elapsed_time(start_time)
        print(f"Time elapsed: {elapsed_time:.2f} seconds")
        
        perform_landing(drone)

if __name__ == '__main__':
    main(sim_key)
