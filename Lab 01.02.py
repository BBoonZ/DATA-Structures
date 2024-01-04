"""Lab 01.02"""
import json
def main(num, aver=0):
    """Lab 01.02"""
    num = [float(i) for i in num]
    _noi = _mak = num[0]
    for i in num:
        if _noi > i:
            _noi = i
        elif _mak < i:
            _mak = i
        aver += i
    tup = (float("%.2f"%_mak), float("%.2f"%_noi), float("%.2f"%(aver/len(num))))
    print(tup)
main(json.loads(input()))
