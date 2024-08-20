import time
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager
sim_key = '79f839c4-48c5-4d6e-9f03-f761e3c63606'

distance = 100

if __name__ == '__main__':

    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        
        start_time = time.time()

        drone.fly_forward(distance, 'cm')
        drone.fly_left(distance, 'cm')
        drone.fly_backward(distance, 'cm')
        drone.fly_right(distance, 'cm')

        end_time = time.time()  # Store the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time

        print(f"Time elapsed: {elapsed_time:.2f} seconds")
        drone.land()
