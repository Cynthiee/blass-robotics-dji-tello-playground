
import time
from djitellopy import tello


drone = tello.Tello()
drone.connect(False) # <- False here

distance = 100

if __name__ == '__main__':
    drone.takeoff()
    start_time = time.time()

    drone.move_forward(distance)
    drone.move_left(distance)
    drone.move_back(distance)
    drone.move_right(distance)

    end_time = time.time()  # Store the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"Time elapsed: {elapsed_time} seconds")
    print(f"Flight Time {int(drone.query_flight_time())}")

    drone.land()
