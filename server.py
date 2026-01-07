from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/emotionDetector')
def detector():
    try:
        query = request.args.get("textToAnalyze")
    except:
        return "Ai, make sure you input text to analyze..."
    
    result = emotion_detector(query)
    if not result or result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    
    if not result["dominant_emotion "]:
        return "Invalid text! Please try again!"
    
    try:
        output = f"""
            For the given statement, the system response is 
            'anger': {result["anger"]}, 
            'disgust': {result["disgust"]}, 
            'fear': {result["fear"]}, 
            'joy': {result["joy"]} 
            and 'sadness': {result["sadness"]}. 
            The dominant emotion is <strong>{result["dominant_emotion"]}</strong>.
        """
    except:
        return "Emotion Detector worked, but could not provide the correct format..."

    return output

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0", 
        port = 5000
    )