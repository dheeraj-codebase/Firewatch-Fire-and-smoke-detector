import streamlit as st
from ultralytics import YOLO
import web_cam
import videos
import images
import tempfile
import os

# Load your pre-trained YOLOv8 model
model_path = "best.pt"
model = YOLO(model_path)

class_names = ["default", "Fire", "smoke"]
temp_dir = tempfile.TemporaryDirectory()


def main():
    st.title("YOLO Object Detection")

    menu = ["Home", "Webcam", "Video", "Image"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown("Welcome to YOLO Object Detection")

    elif choice == "Webcam":
        st.subheader("Webcam Detection")
        web_cam.webcam()

    elif choice == "Video":
        st.subheader("Video Detection")
        video_file = st.file_uploader("Upload Video", type=["mp4", "avi"])
        if video_file is not None:
            temp_video_path = os.path.join(temp_dir.name, video_file.name)
            with open(temp_video_path, "wb") as f:
                f.write(video_file.getbuffer())
            videos.video_detect(temp_video_path)

    elif choice == "Image":
        st.subheader("Image Detection")
        image_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
        if image_file is not None:
            temp_image_path = os.path.join(temp_dir.name, image_file.name)
            with open(temp_image_path, "wb") as f:
                f.write(image_file.getbuffer())
            images.image_detect(temp_image_path)


if __name__ == '__main__':
    main()
