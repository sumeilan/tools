#选择excel文件，讲多个sheets 合并为一个表格，去除空行和重复数据
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import process_data

#选择文件
def choose_file():
	selectFileName = askopenfilename(title='选择文件')  # 选择文件
	e.set(selectFileName)
	print('文件路径是：',selectFileName)

#处理文件
def handle_data():
	source_path = e.get() #要处理的文件路径
	output_path = re.sub(r'.xlsx', r'_test.xlsx',source_path, flags=re.S) #输出的文件路径不变，文件名+test
	process_data.clear_blank_line(source_path,output_path)
	if tkinter.messagebox.askquestion('处理完毕', '文件保存的路径：'+output_path + '\n' +'是否退出？'):
		top.quit()

top = Tk()
top.geometry('500x100')
frame = Frame(top)
top.title ("选择文件")
e = StringVar()
e_entry = Entry(top, width=48, textvariable=e).pack(fill=X,side=LEFT)

submit_button = Button(top,width=10, text="选择文件", command=choose_file).pack(fill=X,side=LEFT,padx=2)
run_button = Button(top,width=10, text="处理数据", command=handle_data).pack(fill=X,side=LEFT,padx=2)
top.mainloop()