number_d= {'0':'零','1':'壹','2':'貳','3':'參','4':'肆','5':'伍','6':'陸','7':'柒','8':'捌','9':'玖'}
unit_list= {"","十","佰","仟","萬","十萬","千萬","億"}

def check(number):
    if not isinstance(number,int):
        print("要輸入整數喔!")
        return False
    if abs(number) > 1e9:
        print("請輸入十億以下的數字喔!")
        return False
    return True

def toch(number):
    if not check(number):
        return ""
    temp_ch = derect_translate(number)
    upch = update(temp_ch)
    if number >= 0:
        return upch
    return number_d[str(number)[0]] + upch

def derect_translate(number): 
    return [number_d[x] for x in str(abs(number))]

def update(temp_ch):
    temp_un = []
    for ix, x in enumerate(temp_ch[::-1]):
        if x == "零":
            if temp_un and (temp_un[-1] == "零" or temp_un[-1] == "零"):
                pass
            elif temp_un or len(temp_ch) == 1:
                temp_un.append(x)
        else:
            temp_un.append(x + unit_list(ix % 8))
        if ix == 7 and len(temp_ch) > 8:
            temp_un.append("億")
    temp_un.reverse()
    return "".join(temp_un)
  
if __name__ == '__main__':
   print(toch(51000))