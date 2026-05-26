# 🐄 Smart Cow Detection System

A simple AI-powered Cow Detection project built using:

- Python
- OpenCV
- YOLOv8
- Ultralytics

This project detects cows in:

- Images
- Videos

using Computer Vision and Deep Learning.

---

# 🚀 Features

✅ Cow Detection in Images  
✅ Cow Detection in Videos  
✅ Bounding Box Visualization  
✅ Confidence Score Display  
✅ Processed Output Saving  
✅ YOLOv8 Integration  
✅ OpenCV Video Processing  

---

# 🛠️ Tech Stack

- Python
- OpenCV
- YOLOv8
- Ultralytics

---

# 📁 Project Structure

```text
SMART-COW-DETECTION/

image_detector.py
video_detector.py
utils.py

input/
├── images/
├── videos/

output/
├── images/
├── videos/
```

---

# ⚙️ Prerequisites

Make sure Python is installed on your system.

---

# 🐍 Check Python Installation

```bash
python3 --version
```

---

# 📦 Install Python (If Not Installed)

## Ubuntu / Linux

```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## Windows

Download Python from:

https://www.python.org/downloads/

IMPORTANT:

While installing Python,
enable:

```text
Add Python to PATH
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SMART-COW-DETECTION.git
```

---

# 📂 Move Into Project Folder

```bash
cd SMART-COW-DETECTION
```

---

# 🌍 Create Virtual Environment

```bash
python3 -m venv myenv
```

---

# ▶️ Activate Virtual Environment

## Linux / Mac

```bash
source myenv/bin/activate
```

---

## Windows

```bash
myenv\Scripts\activate
```

---

# 📚 Install Dependencies

```bash
pip install ultralytics opencv-python
```

---

# ✅ Verify OpenCV Installation

```bash
python3 -c "import cv2; print(cv2.__version__)"
```

---

# ✅ Verify YOLO Installation

```bash
python3 -c "from ultralytics import YOLO; print('YOLO Installed Successfully')"
```

---

# 🤖 YOLO Model

This project uses:

```text
yolov8n.pt
```

The model weights are automatically downloaded by Ultralytics during first run.

No need to manually download the model.

---

# 🖼️ Image Detection

## Run Image Detector

```bash
python3 image_detector.py
```

---

# 🔄 Image Detection Pipeline

```text
Input Image
→ YOLO Inference
→ Detect Cows
→ Draw Bounding Boxes
→ Save Output Image
```

---

# 🎥 Video Detection

## Run Video Detector

```bash
python3 video_detector.py
```

---

# 🔄 Video Detection Pipeline

```text
Input Video
→ Extract Frames
→ YOLO Inference
→ Detect Cows
→ Draw Bounding Boxes
→ Rebuild Video
→ Save Output Video
```
