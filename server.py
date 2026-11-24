''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, request, render_template

# import emotion detection
from emotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detection()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detection.emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    items = [f"'{emotion}': {score}" for emotion, score in list(response.items())[:-1]]

    if len(items) > 1:
        formatted_emotions = ", ".join(items[:-1]) + " and " + items[-1]
    else:
        formatted_emotions = "".join(items)

    return "For the given statement, the system response is " + \
        formatted_emotions + \
        ". The dominant emotion is " + \
        response['dominant_emotion'] + ".\n"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
