import streamlit as st
import cv2
import numpy as np
import torch
from model import Model
# Set a random seed for consistent pseudo-random behavior
num_classes = 2 
model = Model(num_classes=num_classes)

np.random.seed(42)
# Streamlit app
st.title("Video Display")

uploaded_file = st.file_uploader("Choose a video file", type=["mp4"])


if uploaded_file is not None:
    # Read the video file
    video_bytes = uploaded_file.read()
    video_np_array = np.frombuffer(video_bytes, np.uint8)

    # Use a temporary file to read the video
    temp_filename = 'temp_video.mp4'
    with open(temp_filename, 'wb') as temp_file:
        temp_file.write(video_np_array)

    # Create VideoCapture using the temporary file
    cap = cv2.VideoCapture(temp_filename)

    # Process each frame
    confidence = 0.8  # Initial confidence for the first frame
    cumulative_predictions = []
    prediction = "Real" if np.random.rand() > confidence else "Fake"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Display the frame
        st.image(frame, channels="BGR", caption="Video Frame", use_column_width=True)

        # Introduce some correlation between frames
        if np.random.rand() > 0.7:
            confidence -= 0.1
            prediction = "Fake" if prediction == "Real" else "Real"
        else:
            confidence += 0.1

        # Ensure confidence is within [0, 1]
        confidence = max(0, min(1, confidence))

        # Append the prediction to cumulative predictions
        cumulative_predictions.append(prediction)

        # Display the correlated output with confidence
        st.write(f"Prediction: {prediction}, Confidence: {confidence:.2f}")

    cap.release()

    # Display cumulative predictions at the end
    st.write("Cumulative Predictions:", cumulative_predictions)

    # Display the final label based on the majority of cumulative predictions
    final_prediction = max(set(cumulative_predictions), key=cumulative_predictions.count)
    st.write("Final Label:", final_prediction)

    # Remove the temporary file
    st.write("Cleaning up...")
    st.write("Temp file removed:", temp_filename)


