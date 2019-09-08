#埋点数据要检查的项

def compare_act(expect_data,actual_datas):
    if expect_data == actual_datas:
        return True

def compare_pos(expect_data,actual_datas):
    if expect_data == actual_datas:
        return True

# 非必填
def compare_refer(expect_data,actual_datas):
    if expect_data == actual_datas:
        return True

def compare_tag(expect_data,actual_datas):
    if str(expect_data) == str(actual_datas):
        return True

#非必填
def compare_value(expect_data,actual_datas):
    actual_value = list(filter(None, actual_datas))
    expect_value = list(filter(None, expect_data))
    if len(actual_value) == 0 and len(expect_value) ==0:
        return True
    elif len(actual_value) > 0 and len(expect_value) >0:
        return True
    else:
        return False


#非必填
def compare_event_id(expect_data,actual_datas):
    if str(expect_data) == str(actual_datas):
        return True



if __name__ == '__main__':
    pass