import time
from djitellopy import tello


my_drone = tello.Tello()
my_drone.connect()

print(f"Battery Life {my_drone.get_battery()}")

my_drone.takeoff()

time.sleep(30)
print(f"Flight Time {my_drone.query_flight_time()}")
my_drone.flip_forward()