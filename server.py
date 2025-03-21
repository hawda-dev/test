from flask import Flask, request, send_file, jsonify
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_PATH = "downloaded_video.mp4"

@app.route("/download", methods=["POST"])
def download_video():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # yt-dlp options
        ydl_opts = {
            "outtmpl": DOWNLOAD_PATH,
            "format": "best"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return send_file(DOWNLOAD_PATH, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
