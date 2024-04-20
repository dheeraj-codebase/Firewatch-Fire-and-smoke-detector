import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration, WebRtcMode
from ultralytics import YOLO
import cv2

class VideoTransformer(VideoProcessorBase):
    def __init__(self):
        pass

    def transform(self, frame):
        self.class_names = ["Fire", "default", "smoke"]
        self.model = YOLO("best.pt")
        results = self.model(frame)
        annotated_frame = results[0].plot()
        new_frame = annotated_frame.copy()
        for a in results:
            b = a.boxes.data.tolist()
            if len(b) > 0:
                x1, y1, x2, y2, conf, cls = b[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                label = self.class_names[int(cls)]
                color = (0, 255, 0) if label == "default" else (0, 0, 255)
                cv2.rectangle(new_frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(new_frame, f"{label}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        self.frames.append(new_frame)
        st.write("Check!!")
        return new_frame

def main():
    st.title("Detect Fire & Smoke")

    webrtc_ctx = webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTCConfiguration(
            {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
        ),
        video_processor_factory=VideoTransformer,
        async_transform=True  # Set async_transform to False
    )

    if webrtc_ctx.video_transformer:
        st.error("Your webcam is active!!")
        st.write(len(webrtc_ctx.video_transformer.frames))
        if len(webrtc_ctx.video_transformer.frames) > 0:
            st.write("Inside the IF loop!!")
            st.image(webrtc_ctx.video_transformer.frames[-1], caption='Processed Frame', use_column_width=True)


if __name__ == "__main__":
    main()
