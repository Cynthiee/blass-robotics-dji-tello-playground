import time
from djitellopy import tello
import cv2


drone = tello.Tello()
drone.connect(False)

drone.takeoff()
drone.move_up(35)

drone.streamoff()
drone.streamon()


img = drone.get_frame_read().frame
img = cv2.resize(img, (640, 480))

# cv2.imshow("Image", img)
cv2.imwrite("Selfie.jpg", img)


while True:
    hover_time = 20
    time.sleep(hover_time)

    print("_______________________")
    print("------------------------")
    if cv2.waitKey(5) & 0xFF == ord('q'):
        drone.streamoff()
        break

drone.land()
cv2.destroyAllWindows()
    

