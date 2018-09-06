# coding: utf-8
import numpy as np
import matplotlib.pylab as plt
import cmath
import math
import random

#パラメータ群
T0 = 1
alph = 1
#分割数(T0をDIVで分割(プログラム上はそのぶんだけ時間延長みたいに引き延ばす)して計算する。この値が大きいとグラフがカクカクしてくる)
DIV = 10*T0;

#インパルス応答
def h(t):
    if (math.pi*t/T0) == 0:
        return 1/T0
    #計算精度の問題で、桁落ちして0になることがあるっぽいので対策
    elif (math.pi**2 -4*(alph*math.pi*t/T0)**2) == 0:
        return -1
    else :
        return (math.pi ** 2 /T0) *(math.sin(math.pi*t/T0)/(math.pi*t/T0)) *math.cos(alph*math.pi*t/T0) /(math.pi**2 -4*(alph*math.pi*t/T0)**2)

#numpyのndarrayを流し込んでもいいようにvectorize
vh = np.vectorize(h)

print ( "%lf" ,h(0))
print ( "%lf" ,h(1))

#インパルス応答の波形を計算
x = np.arange(-10,10,0.1)
impulseRes = vh(x)

#入力波形をランダム生成する
input = np.ones(1)
len = 100
interval = DIV
len = len*interval + len
count = 0
for i in range(len):
    count = count + 1
    if count == interval :
        count = 0
        tmp = (1) if (random.randint(0,1)) == 1 else -1
        input = np.append(input, tmp)
    else :
        input = np.append(input, 0)

#畳み込みで出力を計算
output = np.convolve(input, impulseRes)
#plt.plot(output, label= "α=0")

#グラフを周期的に重ねて描画する
count = DIV*2
while count <= len:
    plt.plot(output[count - DIV*2 : count])
    count = count + DIV*2

plt.xlabel("t")
plt.ylabel("output")
plt.show()
