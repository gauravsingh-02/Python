# Real-Time Facial Expression Detection

This repository contains a Python script for real-time facial expression detection using OpenCV and DeepFace. The script captures video from your computer's camera, analyzes each frame to predict facial expressions, and overlays the dominant emotion on the video feed.

## Prerequisites

Make sure you have the following dependencies installed before running the script:

- OpenCV: `pip install opencv-python`
- DeepFace: `pip install deepface`

**Note:** Save the `exp.py` file and the shape predictor `shape_predictor_68_face_landmarks.dat` in the same directory as the script. You can download the shape predictor file from [here](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2).

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/gauravsingh-02/Python
    cd Expression
    ```

2. Run the script:

    ```bash
    python exp.py
    ```

3. Press 'q' to exit the application.

## How it works

The script uses OpenCV to capture video frames from the default camera (usually the built-in webcam). It then utilizes the DeepFace library to perform facial expression analysis on each frame. The dominant emotion predicted by DeepFace is overlayed on the video feed in real-time.

## Additional Configuration

Save the `exp.py` file and the shape predictor `shape_predictor_68_face_landmarks.dat` in the same directory as the script.

## Acknowledgments

- [OpenCV](https://opencv.org/): Open Source Computer Vision Library
- [DeepFace](https://github.com/serengil/deepface): A deep learning framework for face analysis

Feel free to leave your reviews or suggestions! I appreciate your feedback.

Happy coding!
