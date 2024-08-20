from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager
 
if __name__ == '__main__':
 
    sim_key = '7e5b7c98-c099-4aa0-a216-e018c696bc8f'

    distance = 40

    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.fly_forward(distance, 'in')
        drone.fly_left(distance, 'in')
        drone.fly_backward(distance, 'in')
        drone.fly_right(distance, 'in')
        drone.flip_backward()
        drone.land()