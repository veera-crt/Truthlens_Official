from flask import Flask, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os

from ingestion import get_trending_data

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/trending")
def trending():
    videos = get_trending_data()
    results = []
    
    for v in videos:
        results.append({
            "title": v["title"],
            "channel": v["channel"],
            "channel_type": "Verified" if int(v.get("subscribers", 0)) > 1000000 else "Moderate" if int(v.get("subscribers", 0)) > 10000 else "Unverified",
            "views": int(v.get("views", 0)),
            "likes": int(v.get("likes", 0)),
            "thumbnail": v["thumbnail"]
        })
        
    return jsonify(results)

@app.route("/live_viral_stream")
def live_viral_stream():
    videos = get_trending_data()
    stream_data = []
    for v in videos:
        stream_data.append({
            "title": v["title"],
            "views": int(v.get("views", 0))
        })
    return jsonify(stream_data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


