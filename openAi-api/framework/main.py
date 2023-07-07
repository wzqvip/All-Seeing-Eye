from flask import Flask, request, jsonify, send_from_directory,send_file
from flask_cors import CORS  # 新增这一行
import openai
import lib.jobfinding as jobfinding
import os
from images import imagegeneration
from images.convert import convert_json_to_png
import lib.api_functions as functions
from pathlib import Path

KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = KEY


app = Flask(__name__)
CORS(app)

VOICE_DIR =Path.cwd() / "openAI-api" / "framework" / "voices"
IMAGE_DIR = Path.cwd() / "openAI-api" / "framework" / "images" / "images"
img_name = 'img_gen'
output_img_name = ""
 #x.__dict__()['result'][:5]

# @app.route('/api/get_image/<filename>')
@app.route('/api/get_image', methods=['GET'])
def get_image():
    # 假设你的图片文件位于服务器的 "IMAGE_DIR" 文件夹
    # while(output_img_name==""):
    #     pass
    return send_file(IMAGE_DIR / output_img_name, mimetype='image/png')
    # return send_from_directory(IMAGE_DIR, output_img_name, as_attachment=True)

@app.route('/api/uploadMP3', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save( VOICE_DIR /'voice.mp3')

@app.route('/api', methods=['POST'])
def process():
    data = request.get_json()  # 获取前端发送的数据
    m_type = data.get('type')  # 获取字典中的'text'字段
    m_is_audio_input = data.get('is_audio_input')
    # m_is_video_input = data.get('is_video_input')
    m_audio_input = None
    # m_video_input = None
    # GET CONTENT
    m_content = None

    if (m_is_audio_input):
        # m_audio_input = data.get('audio_input')  # mp3?
        # m_content = functions.derive_text_from_audio(m_audio_input)
        # you should use url request to get the audio file
        audio_file= open(VOICE_DIR / 'voice.mp3', "rb")
        m_content = openai.Audio.transcribe("whisper-1", audio_file)['text']
    # elif(m_is_video_input):
    #     m_video_input=data.get('video_input') #mp4?
    else:
        m_content = data.get('content')


    if (m_type == 0):
        processed_text = "test"
    elif (m_type == 1):
        # 你的处理逻辑
        processed_text = functions.calculate_job(m_content)
    elif (m_type == 2):
        # 你的处理逻辑
        processed_text = functions.give_instruction(m_content)
    elif (m_type == 3):
        processed_text = functions.predict_future(m_content)
    

    if (data.get('gen_img')):
        json_name = imagegeneration.generate(img_name)
        json_img_path = imagegeneration.DATA_DIR / (json_name + '.json')
        global output_img_name
        output_img_name = json_name + '.png'
        png_img = convert_json_to_png(json_img_path)
        m_image = (IMAGE_DIR / (json_name + '.png')).__str__()
    else:
        m_image = None

    # 将处理结果返回给前端
    return jsonify({'type': m_type, 'result': processed_text, 'image': m_image})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
