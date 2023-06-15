num = 123456789765112300000000003331
k = []
digit_count = len(str(num))
dia = len(str(num))

while digit_count > 4:
    o = 4
    print(num)
    j = num % 10**o  

    k.append(j)
    digit_count = digit_count - 4
    print(k)
    print(j)
    num = num // 10**o  
    print(num)

if digit_count <= 4:
    k.append(num)
    print(k)
s = int(dia / 4)
ui = dia / 4
print(ui)
if ui <= 1:
    print("%d" % (k[0]))
if 1 < ui <= 2:
    print("%d만%d" % (k[1], k[0]))
if 2 < ui <= 3:
    print("%d억%d만%d" % (k[s], k[1], k[0]))
if 3 < ui <= 4:
    print("%d조%d억%d만%d" % (k[3], k[2], k[1], k[0]))
if 4 < ui <= 5:
    print("%d경%d조%d억%d만%d" % (k[4], k[3], k[2], k[1], k[0]))
if 5 < ui <= 6:
    print("%d해%d경%d조%d억%d만%d" % (k[5], k[4], k[3], k[2], k[1], k[0]))
if 6 < ui <= 7:
    print("%d자%d해%d경%d조%d억%d만%d" % (k[6], k[5], k[4], k[3], k[2], k[1], k[0]))
if 7 < ui <= 8:
    print("%d양%d자%d해%d경%d조%d억%d만%d" % (k[7], k[6], k[5], k[4], k[3], k[2], k[1], k[0]))
if 8 < ui <= 9:
    print("%d양%d자%d해%d경%d조%d억%d만%d" % (k[8],k[7], k[6], k[5], k[4], k[3], k[2], k[1], k[0]))
if 9 < ui <= 10:
    print("%d양%d자%d해%d경%d조%d억%d만%d" % (k[9],k[8],k[7], k[6], k[5], k[4], k[3], k[2], k[1], k[0]))
if 10 < ui <= 11:
    print("%d양%d자%d해%d경%d조%d억%d만%d" % (k[10],k[9],k[8],k[7], k[6], k[5], k[4], k[3], k[2], k[1], k[0]))