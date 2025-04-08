import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, detection_confidence=0.8, tracking_confidence=0.8):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1,
                                         min_detection_confidence=detection_confidence,
                                         min_tracking_confidence=tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def hand_detect(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb_frame)

    def hand_draw(self, result, frame):
        if result.multi_hand_landmarks:
            for hand_landmark in result.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmark, self.mp_hands.HAND_CONNECTIONS)
        return frame
