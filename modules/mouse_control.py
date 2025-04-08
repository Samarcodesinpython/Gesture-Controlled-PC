import pyautogui

class MouseControl:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()

    def move_cursor(self, screen_x, screen_y):
        screen_x = max(10, min(self.screen_width - 10, screen_x))
        screen_y = max(10, min(self.screen_height - 10, screen_y))
        pyautogui.moveTo(screen_x, screen_y, duration=0.1)

    def perform_click(self):
        pyautogui.click()

    def pause_play(self):
        pyautogui.press('space')

    def scroll(self, direction):
        pyautogui.scroll(direction)

    def stop_action(self):
        pass  # hook here if needed

    def zoom_in(self):
        pyautogui.hotkey('ctrl', '+')

    def zoom_out(self):
        pyautogui.hotkey('ctrl', '-')
