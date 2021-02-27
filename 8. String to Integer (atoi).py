import re
def myAtoi(w):
    w=w.strip()
    pattern = r"^[-+]?[\d]+"
    result = re.findall(pattern, w)
    res=["".join(i) for i in result]
    try:
        if str(res[0]).isdigit():
            if int(res[0])<-2**31:
                return -2**31
            elif int(res[0])>2**31-1:
                return 2**31-1
            else:
                return abs(int(res[0]))
        else:
            if float(res[0])<-2**31:
                return -2**31
            elif float(res[0])>2**31-1:
                return 2**31-1
            else:
                return int(float(res[0]))
    except:
        return 0



w=((input()))
print(myAtoi(w))