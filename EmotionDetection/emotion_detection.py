import requests
import json


def find_dominant(parsed_output: dict):
    """
    Find dominant score in dictionary of emotion-value pairs.
    
    :param parsed_output: Description
    :type parsed_output: dict
    """
    dominant_emotion = max(
        parsed_output, 
        key = parsed_output.get
    )
    parsed_output["dominant_emotion"] = dominant_emotion
    return parsed_output


def parse_result(analyzed_output: str):
    """
    Translate JSON result of API to Dict, and .
    
    :param analyzed_output: Output of Emotion Predict function
    :type analyzed_output: str
    """
    data_raw = json.loads(analyzed_output)
    data_emotions = data_raw["emotionPredictions"][0]["emotion"]
    return data_emotions


def emotion_detector(text_to_analyze: str):
    """
    Input data analyzed on emotion using 
    the Emotion Predict function of the Watson NLP Library.
    
    :param text_to_analyze: String to perform sentiment analysis on
    :type text_to_analyze: str
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = {
        "raw_document": { 
            "text": text_to_analyze 
        }
    }
    response = requests.post(
        url, 
        json = myobj, 
        headers = header)
    
    # JSON API output to dict
    try:
        response_parsed = parse_result(response.text)
    except:
        print("Could not parse output to dict")
        exit()

    # Find dominant emotion
    try:
        response_final = find_dominant(response_parsed)
    except:
        print("Could not find dominant emotion")
        exit()

    return response_final or None


if __name__ == "__main__":
    output = emotion_detector("Does this work?")
    print(output)
