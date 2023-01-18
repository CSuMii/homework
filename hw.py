number= {'0':'零','1':'壹','2':'貳','3':'參','4':'肆','5':'伍','6':'陸','7':'柒','8':'捌','9':'玖'}
unit= {"個","十","佰","仟","萬","十萬","千萬","億"}
numb = int(input('請輸入低於十億的整數數字唷:'))

def check(numb):
    
    if not isinstance(numb, int):
        print("請輸入數字喔")
        return False
    if abs(numb) > 1e9:
        print("我只處理到億唷~")
        return False
    return True

def num2chinese(numb):
    if not check(numb):
        return ""

def count(numb):