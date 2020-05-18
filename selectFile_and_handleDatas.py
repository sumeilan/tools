# 选择excel文件，讲多个sheets 合并为一个表格，去除空行和重复数据
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import process_data
import xlrd
import excel_to_json,format_excel

# 选择文件
def choose_file():
    selectFileName = askopenfilename(title='选择文件')  # 选择文件
    e.set(selectFileName)
    print('文件路径是：', selectFileName)

# 处理文件
def handle_data():
    source_path = e.get()  # 要处理的文件路径
    wb = xlrd.open_workbook(source_path)
    sheets = wb.sheet_names()

    for sheet in sheets:
        datas = excel_to_json.excel_to_json(source_path, sheet)
        name = e.get().split('.xlsx')
        output_path = name[0] + '_' + sheet + '.xlsx'
        process_data.clear_blank_line(output_path, datas, sheet)

    format_excel.format_excel(output_path)
    if tkinter.messagebox.askquestion('处理完毕', '文件已保存到 ' + name[0] + '\n' + '是否退出？'):
        top.quit()

top = Tk()
top.geometry('500x100')
frame = Frame(top)
top.title("选择文件")
e = StringVar()
e_entry = Entry(top, width=48, textvariable=e).pack(fill=X, side=LEFT)

submit_button = Button(top, width=10, text="选择文件", command=choose_file).pack(fill=X, side=LEFT, padx=2)
run_button = Button(top, width=10, text="处理数据", command=handle_data).pack(fill=X, side=LEFT, padx=2)
top.mainloop()
