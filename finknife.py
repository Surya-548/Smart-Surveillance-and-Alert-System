import cv2

def knife_detection():

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Load the cascade
        knife_cascade = cv2.CascadeClassifier('cascade.xml')

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the knives
        knives = knife_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each knife
        for (x, y, w, h) in knives:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

            # Save the image of knife
            img_name = "knife_detected.jpg"
            cv2.imwrite(img_name, frame)

            print("Knife detected")

        # Display the output
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()