import time
position= 0
wall_location= 5
print("Roomba activated. Beginning forward movement.")
print("---------------------------------------------")
while position<wall_location:
    position+=1
    print(f"Moving... Current position: {position}")
    time.sleep(1)
print("---------------------------------------------")
print("Obstacle detected! Brakes applied.")