from djitellopy import Tello
tello = Tello()

tello.connect()
print(f"Battery is at {tello.get_battery()}%.")
