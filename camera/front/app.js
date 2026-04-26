const BACKEND_URL = "https://your-backend.onrender.com";

function connectCamera() {
    const img = document.getElementById("cameraFeed");
    img.src = BACKEND_URL + "/video";
}