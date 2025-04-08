import cv2
import time

class GestureHUD:
    def __init__(self):
        self.current_gesture = ""
        self.last_update_time = 0

    def update(self, gestures):
        if gestures:
            self.current_gesture = ", ".join(gestures)
            self.last_update_time = time.time()

    def draw(self, frame):
        if time.time() - self.last_update_time < 1.5:
            cv2.putText(frame, f"Gesture: {self.current_gesture}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
