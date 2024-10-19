from djitellopy import Tello

me = Tello()
me.connect()

print("Battery:", me.get_battery())