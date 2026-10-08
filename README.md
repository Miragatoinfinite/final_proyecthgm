# Repository for final project
# Final project

Emotion Detector: a Flask web app that uses the Watson NLP EmotionPredict service to find the emotion in customer feedback.

## Structure

- `EmotionDetection/emotion_detection.py`: the `emotion_detector` function
- `EmotionDetection/__init__.py`: package definition
- `test_emotion_detection.py`: unit tests
- `server.py`: Flask app, route `/emotionDetector`, port 5000
- `templates/index.html` and `static/mywebscript.js`: front end from the starter repo

## Run

```bash
python3 -m pip install requests flask pylint
python3 test_emotion_detection.py
python3 server.py
```

Open `localhost:5000`. Run this inside the Skills Network Theia Lab. The Watson API works only there.

## Output

The app returns scores for anger, disgust, fear, joy and sadness, plus the dominant emotion. Blank input returns `Invalid text! Please try again!`.

