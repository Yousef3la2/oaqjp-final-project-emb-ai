import requests
import json  # Importing json library

def emotion_detector(text_to_analyze):

    # Check if the input is blank
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    # Define the API endpoint and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the input JSON
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the Watson NLP API
    response = requests.post(url, json=input_data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON into a dictionary
        result = response.json()

        # Extract emotion predictions
        emotion_predictions = result.get('emotionPredictions', [])
        
        if emotion_predictions:
            # Get the main emotions for the text
            emotions = emotion_predictions[0].get('emotion', {})

            # Extract scores
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            # Determine the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            # Return the formatted output
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            return "No emotions found"
    else:
        return f"Error: {response.status_code}, {response.text}"