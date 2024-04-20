import streamlit as st
#import web_cam
import web_cam_streamlit_file
import videos
#import videos2
import images
import tempfile
import os


temp_dir = tempfile.TemporaryDirectory()

def main():
    st.title("FireWatch!")
    pg_bg = '''
        <style>
        body {
        background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
        background-size: cover;
        }
        </style>
        '''

    st.markdown(pg_bg, unsafe_allow_html=True)

    menu = ["Home", "Webcam", "Video", "Image"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Home":
        st.caption('_Every fire alarm is a heartbeat, every extinguished flame a saved life._')
        st.caption(':blue[In the ashes of devastation, we find the importance of prevention.]')
        st.subheader("Please choose any of the options from the Menu to continue..")

    elif choice == "Webcam":
        st.subheader("Webcam Detection")
        #web_cam.webcam()
        web_cam_streamlit_file.main()

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
