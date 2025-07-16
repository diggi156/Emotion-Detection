import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load models
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classifier = load_model('emotion_model.h5', compile=False)

# Emotion labels
class_labels = ['Angry','Disgusted','Fearful','Happy','Neutral','Sad','Surprised']

# Webcam setup
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (48,48), interpolation=cv2.INTER_AREA)
        if np.sum(roi) == 0:
            continue

        roi = roi.astype('float32') / 255.0
        roi = np.expand_dims(roi, axis=-1)  # -> (48,48,1)
        roi = np.expand_dims(roi, axis=0)   # -> (1,48,48,1)
        preds = classifier.predict(roi)[0]
        label = class_labels[np.argmax(preds)]
        cv2.putText(frame, label, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)

    cv2.imshow('Emotion Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()