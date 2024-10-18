"""
server.py

This module provides a Flask web application that exposes an API
endpoint for emotion detection in text. The endpoint takes a JSON
input containing text and returns the detected emotions along with 
the dominant emotion.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    """API endpoint to analyze the given text for emotions."""
    data = request.json
    text_to_analyze = data.get("text", "")

    # Check for empty input
    if not text_to_analyze:
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 400

    emotions = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None
    if emotions['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Constructing the response text
    response_text = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': emotions['dominant_emotion'],
        'message': (
            f"For the given statement, the system response is "
            f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
            f"'sadness': {emotions['sadness']}. The dominant emotion is "
            f"{emotions['dominant_emotion']}."
        )
    }

    return jsonify(response_text), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
