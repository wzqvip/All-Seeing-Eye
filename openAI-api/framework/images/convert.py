# convert.py

import json
from base64 import b64decode
from pathlib import Path
import os
# DATA_DIR = Path.cwd() / "responses"
# JSON_FILE = DATA_DIR / "An ec-1667994848.json"
# IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem
def main():
    DATA_DIR =  Path.cwd()/"openAI-api"/"framework"/"images"/"responses"

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            JSON_FILE =  DATA_DIR / filename
            IMAGE_DIR =  Path.cwd()/"openAI-api"/"framework"/ "images" / "images"

            IMAGE_DIR.mkdir(parents=True, exist_ok=True)

            with open(JSON_FILE, mode="r", encoding="utf-8") as file:
                response = json.load(file)

            for index, image_dict in enumerate(response["data"]):
                image_data = b64decode(image_dict["b64_json"])
                image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
                with open(image_file, mode="wb") as png:
                    png.write(image_data)
if __name__ == "__main__":
    main()

def convert_json_to_png(json_img,IMAGE_DIR =  Path.cwd()/"openAI-api"/"framework"/ "images" / "images"):
    with open(json_img, mode="r", encoding="utf-8") as file:
        response = json.load(file)
    for index, image_dict in enumerate(response["data"]):
        image_data = b64decode(image_dict["b64_json"])
        image_file = IMAGE_DIR / f"{json_img.stem}.png"
        # image_file = IMAGE_DIR / f"{json_img.stem}-{index}.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)
    return image_data