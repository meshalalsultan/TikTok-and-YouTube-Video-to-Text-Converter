This is a Flask web application that allows you to extract text from a YouTube video or an uploaded video file.

Requirements
Python 3.x
Flask
youtube-dl
moviepy
speechrecognition
Installation
Clone the repository: git clone https://github.com/your_username/video-to-text.git
Move to the project directory: cd video-to-text
Create a virtual environment: python -m venv venv
Activate the virtual environment: source venv/bin/activate (on Windows: venv\Scripts\activate)
Install the dependencies: pip install -r requirements.txt
Run the Flask app: python app.py
Go to http://localhost:5000 in your web browser.
Usage
Extract text from a YouTube video
Copy the URL of the YouTube video you want to extract the text from.
Paste the URL in the input field in the home page of the web app.
Click on the "Get Text" button.
Wait for the app to extract the text from the video.
The text will be displayed on the page.
Extract text from an uploaded video file
Click on the "Upload Video" button in the home page of the web app.
Select the video file you want to upload.
Click on the "Upload" button.
Wait for the app to extract the text from the video.
The text will be displayed on the page.
Troubleshooting
If you encounter an error related to youtube-dl or moviepy, try updating them to the latest version: pip install --upgrade youtube-dl moviepy
If you encounter an error related to speechrecognition, try installing the following dependencies:
For Linux: sudo apt-get install python3-pyaudio portaudio19-dev
For macOS: brew install portaudio && pip install pyaudio
For Windows: download and install the PyAudio wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
