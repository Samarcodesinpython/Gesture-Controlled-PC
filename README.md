🖱️ Gesture Mouse - AI Powered Touchless Controller
Control your computer like a boss using only your hand gestures — no mouse, no touch, just ✋🧠💻.



🚀 Overview
Gesture Mouse is an AI-powered, touchless mouse controller built using MediaPipe and OpenCV. It lets you move your cursor, click, scroll, zoom, switch tabs, play/pause media — all with just your hand gestures captured through a webcam.

Whether you're flexing futuristic vibes in front of your laptop or working hands-free — this project brings that Minority Report tech into reality.

✨ Features
🖱️ Move cursor with your index finger

👆 Tap gesture = Click

✌️ Two-finger scroll (vertical scrolling)

👉👈 Swipe gestures to navigate tabs/windows

🤏 Zoom in/out with gesture

🖐️ Show palm = Play/Pause media

✊ Make a fist = Stop all actions (like an emergency brake)

🎯 Real-time gesture status HUD (heads-up display on screen)

🧠 Built with AI + gesture smoothing to reduce glitches

📂 Project Structure
bash
Copy
Edit
Gesture_Mouse/
├── main.py                      # Main script to run the gesture controller
├── modules/
│   ├── hand_tracker.py         # MediaPipe-based hand detection and tracking
│   ├── mouse_control.py        # Controls cursor & actions like click, scroll, zoom
│   ├── gesture_handler.py      # Detects gestures and maps them to actions
│   └── gesture_hud.py          # Displays detected gesture status on screen
🛠️ Tech Stack
Python

MediaPipe (for hand tracking)

OpenCV (for camera + visualization)

PyAutoGUI (for controlling mouse/keyboard)

Numpy & Math (for processing gesture logic)

📸 Demo
https://user-demo-link-or-gif-here.com

🔧 Installation & Run
bash
Copy
Edit
git clone https://github.com/your-username/Gesture_Mouse.git
cd Gesture_Mouse
pip install -r requirements.txt
python main.py
🧠 Future Upgrades
Eye blink for clicking 👁️

Facial gestures integration

Voice commands + gestures fusion

Custom gesture training with CNN

Multi-hand support

🤝 Contributions
Feel free to fork, star, and contribute! Pull requests and issues are welcome 🙌

📄 License
MIT License
