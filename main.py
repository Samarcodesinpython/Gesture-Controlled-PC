import cv2
from modules.hand_tracker import HandTracker
from modules.mouse_control import MouseControl
from modules.gesture_handler import GestureHandler
from modules.hud_display import GestureHUD

hand_tracker = HandTracker()
mouse_control = MouseControl()
gesture_handler = GestureHandler()
gesture_hud = GestureHUD()

video = cv2.VideoCapture(0)
video.set(3, 1280)
video.set(4, 720)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)

    if not ret:
        break

    frame_height, frame_width, _ = frame.shape
    result = hand_tracker.hand_detect(frame)
    hand_tracker.hand_draw(result, frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            gestures = gesture_handler.detect_gestures(hand_landmarks, frame_width, frame_height, mouse_control)
            gesture_hud.update(gestures)

    gesture_hud.draw(frame)
    cv2.imshow("Gesture Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
