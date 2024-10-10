
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def send_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    emotions = response[0]
    dominant_emotion = response[1]

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    emotion = ""
    for key, value in emotions.items():
        emotion += f"'{key}': {value}, "
    emotion = emotion[:-2]
    result = f"For the given statement, the system response is {emotion}. The dominant emotion is {dominant_emotion}"
    return result

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)