import time

# Variables
target_speed = 50.0
current_speed = 0.0

# This is our "tuning" factor. It determines how aggressive the gas pedal is.
# 0.1 means we apply 10% of the error as throttle.
aggression_factor = 0.1 

print("--- Cruise Control Activated ---")
print(f"Target Speed: {target_speed} km/h\n")

# We will run this loop 20 times to simulate 20 seconds of driving
for second in range(1, 21):
    
    # 1. Calculate how far off we are from our goal
    error = target_speed - current_speed
    
    # 2. Calculate how much throttle to apply based on the error
    throttle_applied = error * aggression_factor
    
    # 3. Apply the throttle to our vehicle's speed
    current_speed = current_speed + throttle_applied
    
    # Print the diagnostics (formatted to 2 decimal places for readability)
    print(f"Sec {second} | Error: {error:.2f} | Throttle Applied: +{throttle_applied:.2f} | Speed: {current_speed:.2f} km/h")
    
    time.sleep(0.5)

print("\n--- Speed Stabilized ---")