import cv2

# 1. Load the built-in Face Detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Open the Webcam
cap = cv2.VideoCapture(0)

print("--- Centric Security Dashboard Active ---")
print("Press 'q' to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to Grayscale for faster processing (Data Analyst best practice)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, "USER", (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Show the window
    cv2.imshow('Face Security', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()