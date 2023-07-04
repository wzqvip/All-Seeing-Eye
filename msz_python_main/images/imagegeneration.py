import json
import os
from pathlib import Path

import openai

PROMPT = "An android with blob on forehead working in a bar in the environment like Cyberpunk 2077"
# DATA_DIR = Path.cwd() / "responses"
DATA_DIR = Path.cwd() / "msz_python_main"/ "images" / "responses"

DATA_DIR.mkdir(exist_ok=True)

openai.api_key="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"

#图片返回格式设置成b64_json,
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
    response_format="b64_json",
)

#构建json文件路径名称
file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

# 写文件，保存文件
with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)