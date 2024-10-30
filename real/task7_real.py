import time
from djitellopy import tello


drone = tello.Tello()
drone.connect(False) # <- False here

distance = 60

if __name__ == '__main__':
    drone.takeoff()
    drone.move_up(30)
    drone.streamoff()
    drone.streamon()

    drone.move_forward(distance)
    while True:

        img = drone.get_frame_read().frame
        img = cv2.resize(img, (640,480))

    
        cv2.imshow("Image", img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            drone.streamoff()
            break
   

    drone.land()
