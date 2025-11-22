# 🎵 Virtual-Drum Using OpenCV & Python

A simple AI-based Air Drum application that uses OpenCV, color detection, and pyautogui to trigger keyboard events based on hand-controlled positions. By moving a blue object (such as a glove or marker) in front of your webcam, you can play drum sounds mapped to keyboard keys.

## 📌 Features

- 🎯 Real-time color detection using OpenCV (HSV mask)

- 🥁 Virtual drum pads displayed on screen

- ⌨️ Automatic key presses triggered by your movement

- 📸 Webcam-based tracking (no special hardware needed)

- ⚡ Lightweight and easy to run

## 🛠️ Technologies Used

- Python

- OpenCV

- NumPy

- PyAutoGUI

- Imutils

## 🚀 How It Works

- The webcam captures your video feed.

- OpenCV converts the frame to HSV color space.

- A mask is applied to detect blue-colored objects.

- When the detected object enters specific regions on the screen, a keyboard key is triggered using pyautogui.keyDown().

- You can map these keys to drum sounds in any DAW or drum software.


## 🎮 Drum Pad Key Mapping

| Drum Pad Region | Key Mapping |
|-------|-------------|
| **Crash (Top-Left)** | 9 |
| **Tom 2 (Top-Middle)** | w |
| **Ride (Top-Right)** | 7 |
| **Hi-Hat (Left-Top)** | 5 |
| **Snare (Left-Bottom)** | 2 |
| **Tom 3 (Right-Top)** | e |
| **Kick (Right-Bottom)** | 1 |



## 🧩 Setup & Installation
- 1️⃣ Install Dependencies
  - pip install opencv-python numpy pyautogui imutils

- 2️⃣ Run the Script
  - python air_drum.py

- 3️⃣ Use a Blue Object

Wave a blue-colored item in front of the camera to hit drum pads.

Make sure to open an drum website in the background as the pyhon file just Detects as activates the coresponding key the music itself is produced by external website.You can cange the mapping to match the website key mapping to get optimal results

## 📝 Code Overview

- HSV Masking: Detects blue color

- Contours & Bounding Box: Tracks position and size

- Virtual Drum Layout: Displayed using OpenCV circles & labels

- Key Events: Sent via PyAutoGUI

## ❗ Notes

- Ensure proper lighting for accurate color detection.

- You may need to adjust HSV values to match your blue object.

- Works best at 720p or lower resolution for performance.
