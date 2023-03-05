# TikTok and YouTube Video to Text Converter
 
# Video to Text Flask App

This Flask app allows users to extract text from a YouTube video or a video file uploaded from their machine.

## Getting Started

These instructions will guide you on how to set up and run the Flask app on your local machine.

### Prerequisites

- Python 3.6 or higher
- pip package manager
- virtualenv package (optional)

### Installing

1. Clone the repository to your local machine using the following command:

git clone https://github.com/meshalalsultan/TikTok-and-YouTube-Video-to-Text-Converter


2. Navigate to the project directory:

cd video-to-text-flask-app


3. Create a virtual environment (optional):

virtualenv venv
source venv/bin/activate


4. Install the required packages:

pip install -r requirements.txt


### Running the App

1. Start the Flask app:

flask run


2. Open your web browser and go to the following URL:

http://localhost:5000


The home page of the app should be displayed.

3. To extract text from a YouTube video, enter the video URL in the text box on the home page and click the "Get Text" button.

4. To extract text from a video file uploaded from your machine, click the "Upload Video" button on the home page and select the video file to upload. Once the upload is complete, click the "Get Text" button.

5. The extracted text should be displayed on the next page.

## Built With

- Flask - Python web framework
- youtube-dl - Command-line program to download videos from YouTube and other video sites
- SpeechRecognition - Python library for performing speech recognition with support for several engines and APIs

## License

This project is licensed under the MIT License - see the LICENSE file for details.
