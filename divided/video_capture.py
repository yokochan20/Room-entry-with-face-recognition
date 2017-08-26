i
port cv2

cap = cv2.VideoCapture(0)
code = cv2.waitKey(0) & 0xFF

def capture():
    while (cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(100,100),flags = cv2.CASCADE_SCALE_IMAGE)
        if frame is None:
            continue

        if code == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

capture()
