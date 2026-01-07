from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route('/emotionDetector')
def detector():
    try:
        query = request.args.get("textToAnalyze")
    except:
        return "Ai, make sure you input text to analyze..."
    try:
        result = emotion_detector(query)
    except:
        return "Emotion Detector failed..."
    try:
        output = f"""
            For the given statement, the system response is 
            'anger': {result["anger"]}, 
            'disgust': {result["disgust"]}, 
            'fear': {result["fear"]}, 
            'joy': {result["joy"]} 
            and 'sadness': {result["sadness"]}. 
            The dominant emotion is {result["dominant_emotion"]}.
        """
    except:
        return "Emotion Detector worked, but could not provide the correct format..."


    return output