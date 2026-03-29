import cv2
import numpy as np

def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam nedetectat.")
        return

    ratio_history = []

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Nu s-a putut citi frame-ul")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        for (x, y, w, h) in faces:
            face_roi = frame[y:y+h, x:x+w]
            gray_roi = gray[y:y+h, x:x+w]

            # Apply Canny edge detection to face ROI
            edges = cv2.Canny(gray_roi, 50, 150)
            
            # Find contours in edges
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                # Find largest contour assuming it s face outline
                largest_contour = max(contours, key=cv2.contourArea)

                # Approximate contour to reduce points
                approx = cv2.approxPolyDP(largest_contour, 0.01 * cv2.arcLength(largest_contour, True), True)

                # Get bounding rect of approximated contour
                (cx, cy, cw, ch) = cv2.boundingRect(approx)

                # Compute ratio from contour bounding box (more precise than original bbox)
                contour_ratio = ch / cw
                ratio_history.append(contour_ratio)
                if len(ratio_history) > 100:  # moving average over last 50 frames
                    ratio_history.pop(0)

                avg_ratio = np.mean(ratio_history)

                # More nuanced thresholds
                if avg_ratio > 1.4:
                    shape = "Oval"
                elif 1 < avg_ratio <= 1.4:
                    shape = "Rectangular"
                elif 0.85 <= avg_ratio <= 1:
                    shape = "Round"
                else:
                    shape = "Wide"

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, f"{shape} ({avg_ratio:.2f})", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('Face Shape Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
