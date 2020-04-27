import numpy as n
import cv2 as c

# Enter data here
data = 'ABMNOPQabcdefghijklmop q1234567890{}[]:";?>zZ'

k = 0

# image array 3-Dimensional
a = n.zeros((100, 100, 3), dtype=int)
(r, co, p) = a.shape

'''
This is a dictionary I used to convert the most significant
value since int values does not exist as 00 and 01
I used 20 for 00 and 21 for 01
'''


def msp(val):
    dataDic = {'00': 20, '01': 21, '0': 0, '1': 1, '10': 10, '11': 11}
    return dataDic[val]


# Splitting the data into r,g,b
for i in range(r):
    for j in range(co):
        if k < len(data):
            num = bin(int.from_bytes(data[k].encode(), 'big'))[3:] # [3:]Removing the ob1 of binary format
            a[i][j][0] = msp(num[0:-4])
            a[i][j][1] = int(num[-4:-2])
            a[i][j][2] = int(num[-2:])
            k += 1
        else:
            # This part is for the end point in the message transmitted
            a[i][j][0], a[i][j][1], a[i][j][2] = 11, 11, 11
            break

# Saving the data as image
a = a.astype(n.uint8)
c.imwrite(r'pic.png', a)
