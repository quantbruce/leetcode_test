###### 很坑爹，又是本地可以通过，上限提交就不通过。
###### 自己对class Solution 这方面，原理及其应用掌握的不是很透彻

# raw_str = "abbbbbbAAAdcdddd"
raw_str = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBeeeeeeeeeeFYHHnjHAPQQc"

dic = {4:'a',5:'b',6:'c',7:'d',8:'e',9:'f',10:'g',11:'h',12:'i',13:'j',14:'k',15:'l',16:'m',17:'n',18:'o',19:'p',20:'q',21:'r',22:'s',23:'t',24:'u',25:'v',26:'w',27:'x',28:'y',29:'z',
       30:'A',31:'B',32:'C',33:'D',34:'E',35:'F',36:'G',37:'H',38:'I',39:'J',40:'K',41:'L',42:'M',43:'N',44:'O',45:'P',46:'Q',47:'R',48:'S',49:'T',50:'U',51:'V',52:'W',53:'X',54:'Y',55:'Z'}


def compress(raw_str):
    raw_str += '#'
    i, j = 0, 1
    res = ''
    while raw_str[j] != '#':
        while raw_str[i] != raw_str[j]:
            res += raw_str[i]
            i += 1
            if raw_str[j] != '#':
                j += 1
            else:
                break
        while raw_str[i] == raw_str[j]:
            j += 1
        if 4 <= len(raw_str[i:j]) <= 55:
            res = res + '0' + dic[len(raw_str[i:j])] + raw_str[i]
            i = j
            if raw_str[j] != '#':
                j += 1
            else:
                break
        elif len(raw_str[i:j]) < 4:
            res = res + raw_str[i:j]
            i = j
            if raw_str[j] != '#':
                j += 1
            else:
                break
        elif len(raw_str[i:j]) > 55:
            chushu = len(raw_str[i:j]) // 55
            yushu = len(raw_str[i:j]) % 55
            res += ('0Z' + raw_str[i]) * chushu + '0' + dic[yushu] + raw_str[i]
            i = j
            if raw_str[j] != '#':
                j += 1
            else:
                break
    if raw_str[j] == '#' and j-1 == i:
        res += raw_str[i]
    return res

print(compress(raw_str))
