"""Flask web server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the main application index page."""
    return render_template('index.html')


@app.route("/emotionDetector")
def sent_detector():
    """Analyze text from request arguments and return formatted emotion scores."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    scores = {k: v for k, v in response.items() if k != 'dominant_emotion'}
    items = list(scores.items())
    total_items = len(items)

    text = "For the given statement, the system response is "

    for i, (emotion, score) in enumerate(items):
        if i == total_items - 1:
            text += f"and '{emotion}': {score}. "
        else:
            text += f"'{emotion}': {score}, "

    text += f"The dominant emotion is {dominant_emotion}."
    return text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
