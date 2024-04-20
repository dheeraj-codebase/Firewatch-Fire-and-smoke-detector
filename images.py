import streamlit as st
from ultralytics import YOLO
import cv2


def image_detect(path):
    # Load pre-trained model
    model = YOLO("best.pt")

    # Class names
    class_names = ["Fire", "default", "smoke"]

    im = cv2.imread(path)

    results = model(im)

    a = results[0].boxes.data.tolist()
    print(a)

    x1, y1, x2, y2, conf, cls = a[0]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    label = class_names[int(cls)]
    # score = f"{conf:.2f}"
    color = (0, 255, 0) if label == "default" else (0, 0, 255)
    cv2.rectangle(im, (x1, y1), (x2, y2), color, 2)
    image_final = cv2.putText(im, f"{label}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    st.image(image_final)
    #cv2.imshow("Detection", im)
    #cv2.waitKey(0)
