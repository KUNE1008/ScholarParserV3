import json
import os
import re
from pathlib import Path

# 敏感信息
sensitive_info_patterns = {
    'Alibaba Cloud AccessKey Secret': r'\b[A-Za-z0-9+/]{40}\b',
    'Alibaba Cloud AccessKey ID': r'\b[A-Za-z0-9_-]{32}\b',
}

def replace_sensitive_info(data_dict):
    for key, pattern in sensitive_info_patterns.items():
        if key in data_dict:
            data_dict[key]["url"] = re.sub(pattern, '***', data_dict[key]["url"])
    return data_dict

input_folder = './data/test_comments/'  # 替换为包含多个JSON文件的文件夹路径
output_file = './tools/output.json'  # 替换为输出合并后JSON文件的路径

merged_data = []
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        with open(os.path.join(input_folder, filename), 'r') as json_file:
            data = json.load(json_file)
            data["citations"] = replace_sensitive_info(data["citations"])
            merged_data.append(data)

with open(output_file, 'w') as output_json:
    json.dump(merged_data, output_json, indent=2)

print('JSON files merged and saved to', output_file)