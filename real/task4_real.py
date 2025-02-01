import time
from djitellopy import tello


drone = tello.Tello()
drone.connect(False)


if __name__ == '__main__':
    
    drone.takeoff()
    
    start_time = time.time()

    x1, y1, z1 = 0, 0, 0  # Starting position (x1, y1, z1)
    x2, y2, z2 = 5, 5, 0  # Ending position (x2, y2, z2)

    
    speed = 15  # Speed in cm/s

    # Check if the arc radius is within the acceptable range
    if abs(x1 - x2) > 10 or abs(y1 - y2) > 10:
        raise ValueError("The arc radius is not within the range of 0.5-10 meters.")

    # Check if both x1/x2, y1/y2, z1/z2 are not between -20-20 at the same time
    if (abs(x1) > 20 or abs(x2) > 20) and (abs(y1) > 20 or abs(y2) > 20) and (abs(z1) > 20 or abs(z2) > 20):
        raise ValueError("Invalid position values. Ensure they are within the range of -20 to 20.")

    # If all checks pass, execute the curve command
    drone.curve_xyz_speed(x1, y1, z1, x2, y2, z2, speed)

    
    end_time = time.time()  # Store the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    drone.land()
