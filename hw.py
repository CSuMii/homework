number= {'0':'零','1':'壹','2':'貳','3':'參','4':'肆','5':'伍','6':'陸','7':'柒','8':'捌','9':'玖'}
unit= {"個","十","佰","仟","萬","十萬","千萬","億"}

def check(num):
    if not isinstance(num, int):
        print("請輸入數字喔")
        return False
    if abs(num) > 1e8:
        print("我只處理到億唷~")
        return False
    return True