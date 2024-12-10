import time
from djitellopy import tello


drone = tello.Tello()
drone.connect(False) # <- False here


if __name__ == '__main__':
    print(f'Battery Percentage: {drone.get_battery}')
    drone.takeoff()
    start_time = time.time()

    hover_time = 15

    #time.sleep(hover_time)
    end_time = time.time()  # Store the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"Time elapsed: {elapsed_time} seconds")
    print(f"Flight Time {drone.query_flight_time()}")

    #drone.land()
