import cv2

cap = cv2.VideoCapture(0)

def video():
    while (cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            continue

        if cv2.waitKey(0) & 0xFF == ord("q"):
            break

        cap.release()
        cv2.destroyAllWindows()

video()
