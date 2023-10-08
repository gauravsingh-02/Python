# HandVolume 2.0

## Overview
HandVolume 2.0 is an advanced version of a hand tracking script designed for setting the volume with a flick of the pinky finger. The script utilizes the MediaPipe library to detect and track hand movements through a webcam, enabling precise volume control.

## Features
1. **Hand Landmark Detection:** Detects and displays landmarks on the hand in real-time.
2. **Finger Tracking:** Tracks finger positions and determines whether they are up or down.
3. **Distance Calculation:** Calculates distances between specified points on the hand.
4. **Volume Control:** Utilizes the flick of the pinky finger to set the volume to the desired level.
5. **Frame Rate Display:** Shows frames per second (FPS) on the display.

## Dependencies
Ensure you have the following Python libraries installed:

- OpenCV: `pip install opencv-python`
- MediaPipe: `pip install mediapipe`

## How to Run
1. **IMPORTANT:** Do not run the module file (`HandTrackingModule.py`). Only run the main script file (`HandVolume2.0.py`).
2. Place both the `HandTrackingModule.py` module file and the `HandVolume2.0.py` script file in the same directory.
3. Install dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the script using:
    ```bash
    python HandVolume2.0.py
    ```

## Controls
- Flick the pinky finger to control and set the volume.
- To close the application, press `q`.

## Advanced Version
This script is customized for setting the volume with a flick of the pinky finger. It builds upon the earlier hand volume tracker, offering specialized functionality.

Feel free to explore and customize the script for your own projects! If you encounter any issues or have suggestions for improvement, please create an issue on GitHub.

Happy coding!
