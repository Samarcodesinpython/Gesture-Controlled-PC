import math
import time

class GestureHandler:
    def __init__(self, cooldown_time=1.2):
        self.last_action_time = {}
        self.cooldown_time = cooldown_time

    def _cooldown(self, gesture):
        now = time.time()
        if gesture not in self.last_action_time or now - self.last_action_time[gesture] > self.cooldown_time:
            self.last_action_time[gesture] = now
            return True
        return False

    def detect_gestures(self, hand_landmarks, frame_width, frame_height, mouse_control):
        gestures = []
        lm = hand_landmarks.landmark

        index_x = int(lm[8].x * frame_width)
        index_y = int(lm[8].y * frame_height)
        thumb_x = int(lm[4].x * frame_width)
        thumb_y = int(lm[4].y * frame_height)

        distance_thumb_index = math.hypot(index_x - thumb_x, index_y - thumb_y)
        is_fist = all(lm[i].y > lm[0].y for i in [4, 8, 12, 16, 20])
        is_palm = all(lm[i].y < lm[0].y for i in [8, 12, 16, 20])
        is_two_finger_scroll = lm[8].y < lm[6].y and lm[12].y < lm[10].y
        is_zoom_gesture = is_fist  # closed hand now for zoom

        mouse_control.move_cursor(index_x * 3, index_y * 2)

        if distance_thumb_index < 40 and self._cooldown("click"):
            mouse_control.perform_click()
            gestures.append("Click")

        elif is_palm and self._cooldown("play_pause"):
            mouse_control.pause_play()
            gestures.append("Play/Pause")

        elif is_two_finger_scroll and self._cooldown("scroll"):
            scroll_direction = -20 if lm[8].y < lm[12].y else 20
            mouse_control.scroll(scroll_direction)
            gestures.append("Scroll")

        elif is_zoom_gesture and self._cooldown("zoom"):
            if distance_thumb_index < 80:
                mouse_control.zoom_in()
                gestures.append("Zoom In")
            else:
                mouse_control.zoom_out()
                gestures.append("Zoom Out")

        return gestures
