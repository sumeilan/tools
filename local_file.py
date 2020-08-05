import webbrowser, os, sys


def open_local_file(file):
    webbrowser.open(file)


def del_local_file(file):
    if os.path.exists(file):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(file)
    else:
        print('no such file:%s' % file)  # 则返回文件不存在


if __name__ == '__main__':
    file = sys.argv[1]
    param = sys.argv[2]
    if param == 'open':
        open_local_file(file)
    elif param == 'del':
        del_local_file(file)

