number_d = {'0':'零','1':'壹','2':'貳','3':'參','4':'肆','5':'伍','6':'陸','7':'柒','8':'捌','9':'玖'}
unit_list = ["","十","佰","仟","萬","十萬","仟萬","億"]

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
            if un and (un[-1] == "零" or un[-1] == "零"):
                pass
            elif un or len(ch) == 1:
                un.append(x)
        else:
            un.append(x + unit_list[ix % 9])
        if ix == 7 and len(ch) > 8:
            un.append("億")
    un.reverse()
    return "".join(un)
  
if __name__ == '__main__':
   print(toch(51235498)+'元整')