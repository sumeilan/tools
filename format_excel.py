from openpyxl.styles import Font
import openpyxl
from openpyxl.styles import Alignment
import os

def format_excel(file):
    workbook = openpyxl.load_workbook(filename=file)
    sheets = workbook.worksheets

    for sheet in sheets:
        skeys = ['A', 'B']
        lkeys = ['C', 'D', 'E', 'F', 'H', 'J', 'K']
        align = Alignment(horizontal='center', vertical='center', wrap_text=True)
        font = Font(name='黑体', size=10, bold=False, italic=False, color='000000')
        for s in skeys:
            sheet.column_dimensions[s].width = 19
        for l in lkeys:
            sheet.column_dimensions[l].width = 29

        for index in range(0, sheet.max_row):
            for cell in list(sheet.rows)[index]:
                cell.font = font
                cell.alignment = align
            index = index + 1
            sheet.row_dimensions[index].height = 40

    workbook.save(file)

if __name__ == '__main__':
    root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    file_name = root + '\\data\\case1.xlsx'
    format_excel(file_name)
