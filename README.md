# Hand Gesture Controlled Volume Modification System

A real-time **AI-powered hand gesture volume control system** that allows users to adjust system volume using hand movements captured through a webcam.

The project uses **Computer Vision** and **Hand Tracking** technologies to create a touchless and interactive audio control experience.

---

## 🚀 Features

- 🎥 Real-time hand tracking
- 🔊 Control system volume using gestures
- ✋ Touchless interaction using webcam
- 🧠 AI-powered hand landmark detection
- ⚡ Smooth and responsive volume adjustment
- 📷 No external hardware required
- 🖥️ Lightweight and efficient implementation

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV** – Video capture & image processing
- **MediaPipe** – Hand tracking and landmark detection
- **Pycaw** – System audio control
- **NumPy** – Mathematical calculations
- **Math Module** – Distance calculations

---

## 📂 Project Structure

```bash
Hand-Volume-Control-System/
│
├── main.py
├── hand_tracking.py
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/hand-volume-control-system.git
cd hand-volume-control-system
```

---

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install opencv-python mediapipe pycaw numpy comtypes
```

---

## ▶️ Usage

Run the project using:

```bash
python main.py
```

Requirements:
- Webcam enabled
- Good lighting conditions
- Hand clearly visible to camera

---

## ✋ Gesture Controls

| Gesture | Action |
|----------|---------|
| Thumb & Index Finger Close | Lower Volume |
| Thumb & Index Finger Far Apart | Increase Volume |
| Open Palm | Stable Volume |
| Closed Fist | Pause Detection |

---

## 🧠 How It Works

1. Webcam captures live video feed.
2. MediaPipe detects hand landmarks.
3. Distance between thumb and index finger is calculated.
4. Finger distance is mapped to system volume range.
5. Pycaw adjusts the system volume accordingly.
6. Real-time visual feedback is displayed on screen.

---

## 🤖 Core Concepts Used

- Computer Vision
- Gesture Recognition
- Human-Computer Interaction
- Real-Time Video Processing
- Audio Automation

---

## 📸 Demo

Add screenshots or GIFs here.

Example:

```bash
assets/demo.gif
```

---

## 🔥 Challenges Faced

- Reducing gesture detection latency
- Achieving smooth volume transitions
- Handling varying lighting conditions
- Improving hand tracking accuracy

---

## 📈 Future Improvements

- Multi-hand gesture support
- Gesture customization
- Voice assistant integration
- Brightness & media control support
- Cross-platform compatibility

---

## 🎯 Applications

- Smart home systems
- Touchless media control
- Accessibility solutions
- AI-powered interfaces
- Interactive presentations

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ayush Sachan**

- AI & Software Engineering Enthusiast
- Interested in Computer Vision, Automation, and AI Systems

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
