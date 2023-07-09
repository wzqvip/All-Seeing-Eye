import json
import ast


def string_to_dict(string):
    # 使用ast.literal_eval()转换字符串为字典
    dict_data = ast.literal_eval(string)
    return dict_data


def string_to_json(string):
    try:
        # 使用json.dumps()转换字典为JSON
        json_data = json.dumps(string_to_dict(string))
        return json_data
    except:
        print("string_to_json error")
        return string

def dict_to_data(dict_data):
    # 使用json.dumps()转换字典为JSON
    try:
        json_data = json.dumps(dict_data)
        return json_data
    except:
        print("dict_to_data error")
        return dict_data