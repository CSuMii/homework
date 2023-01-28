number_d= {'0':'零','1':'壹','2':'貳','3':'參','4':'肆','5':'伍','6':'陸','7':'柒','8':'捌','9':'玖'}
unit= {"","十","佰","仟","萬","十萬","千萬","億"}

def check(number):
    if not isinstance(number,int):
        print("要輸入整數喔!")
        return False
    if abs(number) > 1e9:
        print("請輸入十億以下的數字喔!")
        return False
    return True

def num2chinese(number):
    if not check(number):
        return ""
    ch = derect_translate(number)
    upch = update(ch)
    if number >= 0:
        return upch
    return number_d[str(number)[0]] + upch

def derect_translate(number): 
    return [number_d[x] for x in str(abs(number))]

def update(ch):
    un = []
    for ix, x in enumerate(ch[::-1]):
        if x == "零":
            # 當前位為0時 特殊處理重複零(上一個為零)問題
            if un and (un[-1] == "零" or un[-1] == "零"):
                pass
            elif un or len(ch) == 1:
                un.append(x)
        else:
            un.append(x + unit(ix % 8))
        if ix == 7 and len(ch) > 8:
            un.append("億")
    # print("tmp_inf is ", tmp_inf)    
    un.reverse()
    return "".join(un)
  
if __name__ == '__main__':
   print(num2chinese(51000))