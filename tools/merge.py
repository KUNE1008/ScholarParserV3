import json
import os

input_folder = '../paper_comments/'  # 替换为包含多个JSON文件的文件夹路径
output_file = 'output.json'  # 替换为输出合并后JSON文件的路径

merged_data = []
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        with open(os.path.join(input_folder, filename), 'r') as json_file:
            data = json.load(json_file)
            merged_data.append(data)

with open(output_file, 'w') as output_json:
    json.dump(merged_data, output_json, indent=2)

print('JSON files merged and saved to', output_file)