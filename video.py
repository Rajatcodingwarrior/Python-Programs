import cv2

# Open the video file
cap = cv2.VideoCapture("C:/Users/Rajat Raj/OneDrive/Desktop/python/rajat python programs/video.mp4")

# Check if the video file has been opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Read and display each frame
while True:
    # Capture the current frame
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Display the current frame
    cv2.imshow("Frame", frame)

    # Wait for a key event and break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video file
cap.release()

# Close all windows
cv2.destroyAllWindows()
