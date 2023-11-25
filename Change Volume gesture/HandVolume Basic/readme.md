# Hand Volume Control using Python and OpenCV

Welcome to the Hand Volume Control project! This Python script utilizes the OpenCV library and the MediaPipe Hands module to control the system volume based on hand gestures.

## Overview

This project uses hand tracking to identify the position of the thumb and index finger tips. The distance between these two points is then used to adjust the system volume in real-time. The longer the distance, the higher the volume, and vice versa.

## Requirements

- Python
- OpenCV
- MediaPipe
- NumPy
- PyCaw

Install the required libraries using:

```bash
pip install opencv-python mediapipe numpy pycaw
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/gauravsingh-02/hand-volume-control.git
cd hand-volume-control
```

2. Run the script:

```bash
python hand_volume_control.py
```

3. Interact with the webcam by showing your hand with an open palm. Move your thumb and index finger to control the volume.

## Code Explanation

The script captures video from the webcam, detects hand landmarks using MediaPipe, and calculates the distance between the thumb and index finger tips. This distance is then mapped to a volume range, and the system volume is adjusted accordingly.

A graphical representation of the volume level is displayed on the screen, showing a filled rectangle that represents the current volume percentage.

## Controls

- Press 'q' to exit the application.

## Contributions

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

Happy hand-controlled volume adjusting! 🤚🔊
