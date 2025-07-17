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



Why it's an Al Project:
• Al (Artificial Intelligence) refers to machines mimicking human intelligence.
• Your system uses a camera to "see" faces and "understand" human emotions — a classic example of computer vision and affective computing, both subfields of Al.
So yes — this is definitely an Al project.

Why it's also an ML (Machine Learning) Project:
• You are using a pre-trained deep learning model (CNN) that was trained on the FER-2013 dataset to classify emotions from facial expressions.
• That model learned patterns in data through training - and you're now using it to make predictions on new inputs.
That makes it a proper Machine Learning project too.




## 🚀 How to Run

For MacOS 💻🍎
cd ~/Emotion-Detection

source venv/bin/activate

python3 test.py


For Windows 🖥️
Download ANACONDA 


## 1. Clone the repository


1. D: ✅ cd Emotion-Detection

2. Create and activate virtual environment (recommended)
conda create -n emotion-env python=3.10

    ✅ conda activate emotion-env
   
    [(emotion-env) D:\Emotion-Detection>]

4. Install dependencies
pip install -r requirements.txt

5. Run the application

    ✅ python test.py

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
