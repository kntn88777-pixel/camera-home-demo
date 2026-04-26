from flask import Flask, Response, jsonify
from camera import Camera

app = Flask(__name__)

camera = Camera()

@app.route("/")
def home():
    return jsonify({"status": "Camera backend running"})

@app.route("/video")
def video():
    return Response(camera.generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)