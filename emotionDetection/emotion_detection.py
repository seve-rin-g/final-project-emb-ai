import requests, json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze):
    ''' Returns the EMOTION detected in text_to_analyze 
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    
    scores = formatted_response['emotionPredictions'][0]["emotion"]
    
    scores['dominant_emotion'] = max(scores, key=scores.get)

    return scores

