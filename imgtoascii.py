import sys
import cv2
file = cv2.imread(sys.argv[1])
try:
    scal = int(sys.argv[2])
except:
    scal = 25

 #   array1 = height,            2 = width,                3 = color
 #len(file) = height, len(file[0]) = length, len(file[0][0]) = color  
 #resizeparam-fx=height,fy=len
          
h = len(file)
l = len(file[0])
c = l/h if(l>h) else h/l
size = (scal,int(scal*c)) if h>l else (int(scal*c),scal)
test=cv2.resize(file, size)

# cv2.imshow('file',file)
# cv2.imshow('test',test)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print(test.shape)
#c1,c2,c3,c4,c5,c6,c7,c8 = "\u2800", "\u2824","\u2832","\u28D4","\u2876","\u28F6","\u28FB","\u28FF"
#c1,c2,c3,c4,c5,c6,c7,c8 = " . ", ". .", ", ;", ": :", ";:;", ":/:", "OOO", "%%%"
c1,c2,c3,c4,c5,c6,c7,c8 = "  ", "..", "**", "==", "##", "%%", "@@", "&&"
temp = 0
print(test[0][0])
for i in range(size[1]):
    temp2=""
    for j in range(size[0]):
        temp=0
        for k in range(3):
            temp+=int(test[i][j][k])
        temp/=3
        if(temp>=0 and temp<32):
            temp2+=c1
        if(temp>=32 and temp<64):
            temp2+=c2
        if(temp>=64 and temp<96):
            temp2+=c3
        if(temp>=96 and temp<128):
            temp2+=c4
        if(temp>=128 and temp<160):
            temp2+=c5
        if(temp>=160 and temp<192):
            temp2+=c6
        if(temp>=192 and temp<224):
            temp2+=c7
        if(temp>=224 and temp<256):
            temp2+=c8
    print(temp2)