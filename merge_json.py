import json
import os

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

	print(data)
	with open('all_json.json', 'w') as f:
		json.dump(data, f)


	# json_file5 = 'E:\\test_python\\tools\\json_data\\5.json'
	# json_file4 = 'E:\\test_python\\tools\\json_data\\4.json'
	# with open(json_file5, 'r') as f:
	# 	json_file5_datas = json.load(json_file5)
	#
	# for x in json_file5_datas:
	# 	data.append(x)
	#
	# with open('all_json.json', 'w') as  f:
	# 	json.dump(data, f)


if __name__ == '__main__':
	read_json()
