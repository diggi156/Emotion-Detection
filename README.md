# Emotion-Detection
Real-time facial emotion detection using Python, OpenCV, TensorFlow, and a pre-trained deep learning model.
# 🎭 Emotion Detection Using AI

Real-time facial emotion detection using deep learning and computer vision. This project uses a pre-trained Mini-XCEPTION model to classify human emotions based on facial expressions via webcam input.

---

## 📌 Features

- 📷 Real-time emotion detection using webcam
- 🧠 Deep learning with pre-trained CNN model (Mini-XCEPTION)
- 🎯 Detects 7 emotions: Angry, Disgusted, Fearful, Happy, Neutral, Sad, Surprised
- ⚡ Fast and efficient using OpenCV and TensorFlow

---

## 🛠️ Technologies Used

- Python 3.10.11
- TensorFlow
- Keras
- OpenCV
- NumPy
- FER-2013 Dataset (for model training)

---

## 📁 Project Structure
Emotion-Detection/
─ test.py                                         # Main script for webcam emotion detection
─ emotion_model.h5                                # Pre-trained Mini-XCEPTION model
─ haarcascade_frontalface_default.xml             # Face detection Haar cascade
─ requirements.txt                                # Python dependencies
─ Emotion_Detection_Project_Report_Digvijoy.docx  # Project report
─ README.md                                       # Project documentation (this file)

---

Download ANACONDA 

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Emotion-Detection.git
cd Emotion-Detection

2. Create and activate virtual environment (recommended)
conda create -n emotion-env python=3.10
conda activate emotion-env

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python test.py

	•	Webcam will open and start detecting emotions in real time.
	•	Press Q to quit the video feed.


😃 Emotion Labels Detected
	•	😠 Angry
	•	😒 Disgusted
	•	😨 Fearful
	•	😄 Happy
	•	😐 Neutral
	•	😢 Sad
	•	😲 Surprised

🔮 Future Enhancements
	•	Deploy as a web app (using Flask or Streamlit)
	•	Add voice-based sentiment analysis
	•	Improve face detection accuracy with MTCNN or Dlib
	•	Train custom models on diverse datasets


📄 License

This project is licensed for educational use. You are free to use, modify, and build upon it.


👨‍💻 Developed By

Digvijoy Ranjan
B.Tech in Computer Science and Engineering
GitHub: https://github.com/diggi156
