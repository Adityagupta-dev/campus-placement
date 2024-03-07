from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load your deepfake detection model here


def detect_deepfake(video_path):
    # Replace this with your actual deepfake detection code
    # This is a placeholder that always returns "Fake" for demonstration purposes
    return "Fake"


@app.route('/')
def index():
    return render_template('landing.html', result=None)


@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return render_template('index.html', result="No video file provided.")

    video = request.files['video']

    if video.filename == '':
        return render_template('index.html', result="No selected video file.")

    if video:
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
        video.save(video_path)
        result = detect_deepfake(video_path)
        os.remove(video_path)  # Remove the uploaded video after processing
        return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
