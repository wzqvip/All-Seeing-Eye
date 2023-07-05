from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def process():
    data = request.get_json()  #获取前端发送的数据
    text = data.get('type')  #获取字典中的'text'字段

    if(type==1):
        # 你的处理逻辑
        processed_text = text.upper()
    elif(type==2):
    # 你的处理逻辑


    return jsonify({'result': processed_text})  #将处理结果返回给前端

if __name__ == "__main__":
    app.run(debug=True)