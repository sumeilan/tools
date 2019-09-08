import json
import os

#多个json文件合并一个json文件
def read_json():
	data = []
	rootdir = 'E:\\test_python\\tools\\json_data'
	list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件

	for i in range(len(list)):
		path = os.path.join(rootdir, list[i])
		print(path)
		if os.path.isfile(path):
			with open(path, 'r') as f:
				i = json.load(f)
				for x in i:
					data.append(x)

	print('data',data)
	with open('E:\\test_python\\tools\\datas\\all_json.json', 'w') as f:
		json.dump(data, f)


if __name__ == '__main__':
	read_json()
