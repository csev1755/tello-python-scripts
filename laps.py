from djitellopy import Tello

x = int(input("How many laps would you like to do? (1-5) \n> ")) # amount of laps

tello = Tello()

tello.connect()
tello.takeoff()

for y in range(x):

    print(f"[INFO] Battery is at {tello.get_battery()}%. {x - y}/{x} laps to go.")
    tello.move_forward(100)
    tello.rotate_counter_clockwise(180)
    tello.move_forward(100)
    tello.rotate_clockwise(180)

tello.land()
