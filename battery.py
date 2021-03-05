from djitellopy import Tello
tello = Tello()

tello.connect()
print(f"[INFO] Battery is at {tello.get_battery()}%.")