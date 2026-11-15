# Robotics Phase 1

An early C++ robotics experiment focused on basic startup and system-status checks.

## Current scope

The current implementation is a small console-based prototype. It runs a sequence of system-check messages with short delays to simulate a basic startup flow.

This repository is an introductory experiment, not a complete robot-control system. It does not currently demonstrate hardware integration, ROS 2, navigation, or autonomous movement.

## Build and run

The repository includes a CMake-based C++ project.

```bash
cmake -S . -B build
cmake --build build
./build/<executable-name>
```

Replace `<executable-name>` with the executable target defined in the project’s `CMakeLists.txt`.

## Project status

This is an early-stage learning project. The next useful improvements are to document the system-check sequence, add focused tests, and keep generated build output out of version control.
