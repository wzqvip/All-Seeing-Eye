from flask import Flask, request, jsonify
import openai
import lib.jobfinding as jobfinding
import os
from images import imagegeneration
import lib.api_functions as functions

KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = KEY


app = Flask(__name__)


@app.route('/1', methods=['POST'])
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
        m_audio_input = data.get('audio_input')  # mp3?
        m_content = functions.derive_text_from_audio(m_audio_input)
    # elif(m_is_video_input):
    #     m_video_input=data.get('video_input') #mp4?
    else:
        m_content = data.get('content')

    m_image = None
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
    try:
        if (data.get('gen_img')):
            m_image = imagegeneration.generate(m_content)
    except:
        m_image = None
    # 将处理结果返回给前端
    return jsonify({'type': m_type, 'result': processed_text, 'image': m_image})


if __name__ == "__main__":
    app.run(port="8081",debug=True)
