import cv2 as c
import numpy

# Reading the image
a = c.imread('pic.png', c.IMREAD_COLOR)

# function that converts 0=>01 and 1=>01
def texRet(frac):
    if frac == 0:
        return '00'
    elif frac == 1:
        return '01'
    else:
        return str(frac)

def msp(val):
    # This is a dictionary I used to decrypt the most significant value
    dataDic = {20: '00', 21: '01', 0: '0', 1: '1', 10: '10', 11: '11'}
    return dataDic[val]

k = 0
(r, co, p) = a.shape
finalStr = ''
# Extracting data from the image
for i in range(r):
    for j in range(co):
        l = msp(a[i][j][0])
        l += texRet(a[i][j][1])
        l += texRet(a[i][j][2])
        sta = int('0b1' + l, 2)
        op = sta.to_bytes((sta.bit_length() + 7) // 8, 'big').decode()
        if sta == 127:
            break
        else:
            finalStr += op
        print(op, sta)
        k += 1

# Extracted data
print(finalStr)
