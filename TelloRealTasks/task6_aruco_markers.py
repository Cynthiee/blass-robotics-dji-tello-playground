from djitellopy import tello
import cv2, sys
import cv2.aruco as aruco
import funcs
import numpy as np
import time


def find_aruco_tags(img, marker_size=4, total_markers=100, draw=True):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    aruco_dict = aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
    aruco_param = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(aruco_dict, aruco_param)

    marker_corners, ids, bad = detector.detectMarkers(img_gray)

    if len(marker_corners) > 0:
        ids = ids.flatten()

        for (corner, id) in zip(marker_corners, ids):

            marker_corners = corner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = marker_corners

            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            # draw the bounding box of the ArUCo detection
            cv2.line(img, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(img, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(img, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(img, bottomLeft, topLeft, (0, 255, 0), 2)
            # compute and draw the center (x, y)-coordinates of the ArUco
            # marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(img, (cX, cY), 4, (0, 0, 255), -1)

            # draw the ArUco marker ID on the image
            cv2.putText(img, str(id),
                (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 2)
            
            print("[INFO] ArUco marker ID: {}".format(id))
            # show the output image
            #cv2.imshow("Image", img)
            cv2.imwrite("ArucoMarker.jpg", img)
            #cv2.waitKey(0)


drone = tello.Tello()
drone.connect(False)

drone.takeoff()
drone.move_up(40)

drone.streamoff()
drone.streamon()


while True:

    img = drone.get_frame_read().frame
    img = cv2.resize(img, (640,480))
    find_aruco_tags(img)
    #time.sleep(10)
    cv2.imshow("Image", img)

   


    cv2.waitKey(1)
