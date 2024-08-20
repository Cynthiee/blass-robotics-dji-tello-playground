import time
from djitellopy import tello


drone = tello.Tello()
drone.connect(False)


if __name__ == '__main__':

    drone.takeoff()
    
    start_time = time.time()
    drone.go_xyz_speed(100, 100, 0, 15)
    drone.go_xyz_speed(100, -100, 0, 15)
    drone.go_xyz_speed(-100, -100, 0, 15)
    drone.go_xyz_speed(-100, 100, 15)

    end_time = time.time()  # Store the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Flight Time {int(drone.query_flight_time())}")
    
    drone.land()
