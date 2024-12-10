import time
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager


sim_key = '47e59214-306e-4c6a-abed-bcf5f3572345'


distance = 100

def read_sim_key_file(filepath):
    with open(filepath, 'r') as file:
        return file.readline().strip()
    
def perform_takeoff(drone):
    """Handles the drone takeoff."""
    drone.takeoff()

def perform_maneuver(drone, distance):
    """Performs a series of maneuvers: forward, left, backward, and right."""
    drone.fly_forward(distance, 'cm')
    drone.fly_left(distance, 'cm')
    drone.fly_backward(distance, 'cm')
    drone.fly_right(distance, 'cm')

def measure_time():
    """Measures the elapsed time for drone operations."""
    start_time = time.time()
    return start_time

def calculate_elapsed_time(start_time):
    """Calculates the elapsed time since a given start time."""
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time elapsed: {elapsed_time:.2f} seconds")

def perform_landing(drone):
    """Handles the drone landing."""
    drone.land()

def main(sim_key, distance):
    """Main function to control the drone."""
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        perform_takeoff(drone)
        
        start_time = measure_time()
        
        perform_maneuver(drone, distance)
        
        calculate_elapsed_time(start_time)
        perform_landing(drone)

if __name__ == '__main__':
    main(sim_key, distance)
