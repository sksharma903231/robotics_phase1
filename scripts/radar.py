print("--- Lidar Scan Initiated ---")
# This is the raw data from our sensor. (Distances in meters)

sensor_data = [12, 15, 2, 20, 5]

# We start by assuming the closest object is a massive number.
closest_object = 999 
# ---------------------------------------------------------
for distance in sensor_data:
    if distance < closest_object:
        closest_object = distance

if closest_object < 3:
    print("CRITICAL: Obstacle too close! Brakes applied.")
else:
    print("Path is clear.")

