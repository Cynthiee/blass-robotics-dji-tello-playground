import time
from djitellopy import tello


drone = tello.Tello()
drone.connect(False) # <- False here

distance = 100

if __name__ == '__main__':
    drone.takeoff()
    start_time = time.time()

    drone.fly_forward(distance, 'cm')
    drone.fly_left(distance, 'cm')
    drone.fly_backward(distance, 'cm')
    drone.fly_right(distance, 'cm')

    end_time = time.time()  # Store the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"Time elapsed: {elapsed_time} seconds")
    print(f"Flight Time {drone.query_flight_time()}")

    drone.land()
