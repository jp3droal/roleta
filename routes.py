from flask import request, send_file, render_template
from pydub import AudioSegment
import os 

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/converter', methods=['POST'])
    def converter():
        file = request.files['file']
        caminho_mp3 = 'audio.mp3'

        file.save('temp.mp4')

        audio = AudioSegment.from_file('temp.mp4', format='mp4')
        audio.export(caminho_mp3, format='mp3')

        os.remove('temp.mp4')

        return send_file(caminho_mp3, as_attachment=True)