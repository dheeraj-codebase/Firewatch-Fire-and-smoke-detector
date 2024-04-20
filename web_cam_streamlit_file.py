import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration, WebRtcMode

class VideoTransformer(VideoProcessorBase):
    def __init__(self):
        pass

    def transform(self, frame):
        # You can perform any processing on the frame here
        return frame

def main():
    st.title("Webcam Access with Streamlit")

    webrtc_ctx = webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTCConfiguration(
            {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
        ),
        video_processor_factory=VideoTransformer,
        async_transform=True
    )

    if webrtc_ctx.video_transformer:
        st.write("Webcam is active")

if __name__ == "__main__":
    main()
