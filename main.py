import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit(-1)

previous_frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    previous_frames.append(frame)

    if len(previous_frames) > 5:
        previous_frame = previous_frames.pop(0)
        previous_frame_inverted = cv.bitwise_not(previous_frame)
        frame = cv.addWeighted(frame, 0.5, previous_frame_inverted, 0.5, 0)

    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
