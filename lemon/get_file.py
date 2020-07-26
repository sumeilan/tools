# -*- coding: utf-8 -*-
import os,sys

#判断文件后缀
def file_type(path):
	file = os.path.splitext(path)
	filename, type = file
	# print(filename,type)
	return type

#获取当前路径下的所有子目录
def files(file_dir):
	for root, dirs, files in os.walk(file_dir):
		# print(root)  # 当前目录路径
		# print(dirs)  # 当前路径下所有子目录
		# print(files)  # 当前路径下所有非目录子文件
		for file in files:
			if file_type(file) == '.html':
				print(file)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        # file = 'E:\\test_python\\testcase\\report'
        files(file_name)


