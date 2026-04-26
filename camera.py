import cv2
import os

class Camera:
    def __init__(self):
        # lấy RTSP từ ENV (an toàn hơn)
        self.url = os.getenv("RTSP_URL", 0)
        self.cap = cv2.VideoCapture(self.url)

    def generate_frames(self):
        while True:
            success, frame = self.cap.read()
            if not success:
                break

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')