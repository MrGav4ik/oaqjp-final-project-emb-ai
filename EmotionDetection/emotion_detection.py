
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        dominant_emotion = None
        emotions = None

    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']

        emotions = {
            'anger': emotion['anger'],
            'disgust': emotion['disgust'],
            'fear': emotion['fear'],
            'joy': emotion['joy'],
            'sadness': emotion['sadness']
        }
    
        dominant_emotion = max(emotions, key=emotions.get)

    return emotions, dominant_emotion

'''
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I hate working long hours.")
'''
