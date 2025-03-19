import cv2
from deepface import DeepFace as df
import numpy as np
import time
import json

cap = cv2.VideoCapture(0)

analysis_interval = 1
last_analysis_time = time.time()

while True:
    _, img = cap.read()
    if not _:
        print('Изображение не найдено')
        break
    current_time = time.time()
    if current_time - last_analysis_time >= analysis_interval:
        try:
            result = df.analyze(img_path=np.array(img), actions=['emotion'])
            print(result[0]['dominant_emotion'])
        except Exception as e:
            print(f"Ошибка: {e}")
        last_analysis_time= current_time
    
    cv2.imshow('',img)
    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows() 