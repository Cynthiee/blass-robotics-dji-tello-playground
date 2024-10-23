import time
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

sim_key = '3161934b-eb8a-423b-b6be-13c1022f1494'

def perform_takeoff(drone):
    """Handles the drone takeoff."""
    drone.takeoff()

def perform_curve_flight(drone):
    """Executes a curved flight maneuver."""
    drone.fly_curve(25, 0, 0, 0, 1, 0, 'in')

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
        
        perform_curve_flight(drone)
        
        elapsed_time = calculate_elapsed_time(start_time)
        print_elapsed_time(elapsed_time)
        
        perform_landing(drone)

if __name__ == '__main__':
    main(sim_key)
