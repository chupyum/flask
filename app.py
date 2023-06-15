from flask import Flask, render_template, request
import os
import openai


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def a():
    return render_template('index.html')

@app.route('/1.html')
def b():
    return render_template('1.html')

@app.route('/13.html')
def z():
    return render_template('13.html')

@app.route('/14.html')
def s():
    return render_template('14.html')

@app.route('/3.html')
def d():
    return render_template('3.html')


@app.route('/17.html')
def e():
    return render_template('17.html')

@app.route('/18.html')
def f():
    return render_template('18.html')

@app.route('/13.html')
def g():
    return render_template('13.html')

@app.route('/50.html')
def h():
    return render_template('50.html')

@app.route('/p.html')
def i():
    return render_template('p.html')

@app.route('/r.html')
def j():
    return render_template('r.html')

@app.route('/t.html')
def k():
    return render_template('t.html')

@app.route('/12.html')
def l():
    return render_template('12.html')

@app.route('/18 - 복사본.html')
def n():
    return render_template('18 - 복사본.html')

@app.route('/18 - 복사본 (2).html')
def m():
    return render_template('18 - 복사본 (2).html')

@app.route('/18 - 복사본 (3).html')
def o():
    return render_template('/18 - 복사본 (3).html')

@app.route('/18 - 복사본 (4).html')
def p():
    return render_template('/18 - 복사본 (4).html')

@app.route('/18 - 복사본 (5).html')
def c():
    return render_template('/18 - 복사본 (5).html')

@app.route('/18 - 복사본 (6).html')
def q():
    return render_template('/18 - 복사본 (6).html')

@app.route('/검색.html')
def r():

    return render_template('검색.html')

@app.route('/rl.html')
def rl():

    return render_template('rl.html')



@app.route('/execute', methods=['POST'])
def execute():
    dk = int(request.form['dk'])
    b = request.form['b']
    c = request.form['c']
    result = None

    if dk == 1:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = a + i
        num=a
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

        if(digit_count<=4):
            k.append(num)
            print(k)
        s=int(dia/4)
        ui=dia/4
        print(ui)
        if(ui<=1):
            result = "%d"%(k[0])
        if(ui>1 and ui<=2):
            result = "%d만%d"%(k[1],k[0])
        if(ui>2 and ui<=3):
            result = "%d억%d만%d"%(k[s],k[1],k[0])
        if(ui>3 and ui<=4):
            result = "%d조%d억%d만%d" %(k[3],k[2],k[1],k[0])
        if(ui>4 and ui<=5):
            result = "%d경%d조%d억%d만%d"%(k[4],k[3],k[2],k[1],k[0])
        if(ui>5 and ui<=6):
            result = "%d해%d경%d조%d억%d만%d"%(k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>6 and ui<=7):
            result = "%d자%d해%d경%d조%d억%d만%d"%(k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>7 and ui<=8):
            result = "%d양%d자%d해%d경%d조%d억%d만%d"%(k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>8 and ui<=9):
            result = "%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>9 and ui<=10):
            result = "%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>10 and ui<=11):
            result = "%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>11 and ui<=12):
            result = "%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k,[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>12 and ui<=13):
            result = "%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>13 and ui<=14):
            result = "%d극%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[13],k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])


    elif dk == 2:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = i ** 2 + a
        
        num=a
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

        if(digit_count<=4):
            k.append(num)
            print(k)
        s=int(dia/4)
        ui=dia/4
        print(ui)
        if(ui<=1):
            result = "%d"%(k[0])
        if(ui>1 and ui<=2):
            result = "%d만%d"%(k[1],k[0])
        if(ui>2 and ui<=3):
            result = "%d억%d만%d"%(k[s],k[1],k[0])
        if(ui>3 and ui<=4):
            result = "%d조%d억%d만%d" %(k[3],k[2],k[1],k[0])
        if(ui>4 and ui<=5):
            result = "%d경%d조%d억%d만%d"%(k[4],k[3],k[2],k[1],k[0])
        if(ui>5 and ui<=6):
            result = "%d해%d경%d조%d억%d만%d"%(k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>6 and ui<=7):
            result = "%d자%d해%d경%d조%d억%d만%d"%(k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>7 and ui<=8):
            result = "%d양%d자%d해%d경%d조%d억%d만%d"%(k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>8 and ui<=9):
            result = "%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>9 and ui<=10):
            result = "%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>10 and ui<=11):
            result = "%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>11 and ui<=12):
            result = "%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k,[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>12 and ui<=13):
            result = "%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>13 and ui<=14):
            result = "%d극%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[13],k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])

    elif dk == 3:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = i ** 3 + a
        num=a
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

        if(digit_count<=4):
            k.append(num)
            print(k)
        s=int(dia/4)
        ui=dia/4
        print(ui)
        if(ui<=1):
            result = "%d"%(k[0])
        if(ui>1 and ui<=2):
            result = "%d만%d"%(k[1],k[0])
        if(ui>2 and ui<=3):
            result = "%d억%d만%d"%(k[s],k[1],k[0])
        if(ui>3 and ui<=4):
            result = "%d조%d억%d만%d" %(k[3],k[2],k[1],k[0])
        if(ui>4 and ui<=5):
            result = "%d경%d조%d억%d만%d"%(k[4],k[3],k[2],k[1],k[0])
        if(ui>5 and ui<=6):
            result = "%d해%d경%d조%d억%d만%d"%(k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>6 and ui<=7):
            result = "%d자%d해%d경%d조%d억%d만%d"%(k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>7 and ui<=8):
            result = "%d양%d자%d해%d경%d조%d억%d만%d"%(k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>8 and ui<=9):
            result = "%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>9 and ui<=10):
            result = "%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>10 and ui<=11):
            result = "%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>11 and ui<=12):
            result = "%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k,[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>12 and ui<=13):
            result = "%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
        if(ui>13 and ui<=14):
            result = "%d극%d재%d정%d백%d간%d구%d양%d자%d해%d경%d조%d억%d만%d"%(k[13],k[12],k[11],k[10],k[9],k[8],k[7],k[6],k[5],k[4],k[3],k[2],k[1],k[0])
    else:
        result = "다시 입력해주세요"

    return render_template('result.html', result=result)



if __name__ == '__main__':
    app.run()

