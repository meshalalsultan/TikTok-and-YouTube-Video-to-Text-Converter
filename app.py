import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tiktok')
def tiktok():
    return render_template('tiktok.html')

@app.route('/download_tiktok', methods=['POST'])
def download_tiktok():
    url = request.form['url']
    cmd = ['tiktok-scraper', url, '-d', 'downloads']
    subprocess.call(cmd)
    return redirect(url_for('index'))

@app.route('/youtube')
def youtube():
    return render_template('youtube.html')

@app.route('/download_youtube', methods=['POST'])
def download_youtube():
    url = request.form['url']
    cmd = ['youtube-dl', url, '-o', 'downloads/%(title)s.%(ext)s', '--verbose']
    subprocess.call(cmd)
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        return redirect(url_for('index'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess
import youtube_dl

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if request.method == 'POST':
        file = request.files['file']
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        ydl_opts = {'outtmpl': 'uploads/%(id)s.%(ext)s', 'format': 'mp4'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(filename, download=True)
            video_url = info_dict.get("url", None)

        return redirect(url_for('video_to_text', video_url=video_url))

@app.route('/video_to_text')
def video_to_text():
    video_url = request.args.get('video_url')

    if video_url:
        process = subprocess.run(['youtube-dl', '-f', 'bestaudio[ext=mp3]/best[ext=mp4]/best', '-o', '-',
                                video_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if not error:
            process = subprocess.Popen(['ffmpeg', '-i', '-', '-f', 's16le', '-ac', '2', '-ar', '44100', '-'],
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate(output)

        if not error:
            process = subprocess.Popen(['deepspeech', '--model', 'models/deepspeech-0.9.3-models.pbmm',
                                        '--scorer', 'models/deepspeech-0.9.3-models.scorer', '--json', '-'],
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate(output)

        if not error:
            result = output.decode('utf-8')
            return redirect(url_for('show_text', text=result))

    return 'Error extracting text from video.'

@app.route('/show_text')
def show_text():
    text = request.args.get('text')
    return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
