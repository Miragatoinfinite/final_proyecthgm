import json	
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = response.json()
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    rp={}
    # Find the emotion with the highest score
    dominant_emotion = max(emotions, key=emotions.get)

    for emotion, score in emotions.items():
        rp[emotion] = score

    dominant_emotion = max(emotions, key=emotions.get)
    rp['dominant_emotion']=dominant_emotion
    
    return rp  # Return the response text from the API
    