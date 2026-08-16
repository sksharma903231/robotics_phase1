import time

x = 0
y = 0
direction = "North"
steps_taken = 0

print("Roomba activated. Navigating the 2D grid.")
print("---------------------------------------------")

while steps_taken < 8:
    
    # 1. THE SENSOR CHECK
    if y == 3 and direction == "North":
        print("wall detected! Turning East.") 
        direction="East"

        
    # 2. THE MOVEMENT LOGIC
    else:
        if direction == "North":
            y = y + 1
        elif direction == "East":
            x = x + 1
            
        print(f"Moving {direction}... Position: (X:{x}, Y:{y})")
        
    steps_taken = steps_taken + 1
    time.sleep(1)