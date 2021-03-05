import cv2
from djitellopy import Tello
tello = Tello()

tello.connect()
tello.takeoff()
tello.streamon()
frame_read = tello.get_frame_read()
tello.move_back(200)
tello.move_up(50)
print("Say cheese!")
cv2.imwrite("picture.png", frame_read.frame)
tello.move_down(50)
tello.move_forward(200)
tello.land()