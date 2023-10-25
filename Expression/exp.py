import cv2
from deepface import DeepFace

# Open a video capture object
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Perform facial expression prediction using DeepFace
    results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    # Check if any face is detected
    if results and 'dominant_emotion' in results[0]:
        # Get the first (and likely the only) result from the list
        result = results[0]

        # Get the predicted emotion
        emotion = result['dominant_emotion']

        # Display the predicted expression
        cv2.putText(frame, f"Emotion: {emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Facial Expression Detection', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()
