from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")

@app.route("/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        cmd = ["yt-dlp", "-f", "best", "-g", url]
        direct_url = subprocess.check_output(cmd).decode("utf-8").strip()
        return jsonify({"success": True, "direct_url": direct_url})
    except subprocess.CalledProcessError:
        return jsonify({"success": False, "error": "Failed to fetch download link. Make sure the link is public."}), 500

@app.route("/")
def serve_index():
    return app.send_static_file("index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
