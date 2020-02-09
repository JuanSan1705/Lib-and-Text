from sys import stdin
import math


def suma(a, b):
    suma1 = a[0] + b[0]
    suma2 = a[1] + b[1]
    return (suma1, suma2)


def producto(a, b):
    mult = [(a[0] * b[0]), (a[0] * b[1]) + (a[1] * b[0]), -(a[1] * b[1])]
    mult1 = (mult[0] + mult[2])
    mult2 = (mult[1])
    return (mult1, mult2)


def resta(a, b):
    resta1 = a[0] - b[0]
    resta2 = a[1] - b[1]
    print('Resta')
    return (resta1, resta2)


def division(a, b):
    b1 = [b[0], -b[1]]
    m = [(a[0] * b1[0]), (a[0] * b1[1]) + (a[1] * b1[0]), -(a[1] * b1[1])]
    m1 = ((b[0] * b1[0]) - (b[1] * b1[1]))
    m2 = (m[0] + m[2])
    m3 = (m[1])
    mResult = m2 / m1
    mResult2 = m3 / m1
    return (mResult, mResult2)


def modulo(a):
    x = math.sqrt((a[0] * a[0]) + (a[1] * a[1]))
    print('Modulo de a')
    return x


def modulob(b):
    s = math.sqrt((b[0] * b[0]) + (b[1] * b[1]))
    print('Modulo de b')
    return s


def conjugado(a):
    con = (a[0], -a[1])
    return (con)


def conjugadob(b):
    con = (b[0], -b[1])
    print('Conjugado de b')
    return (con)


def cartesiano(a):
    x = (a[0] * math.cos(a[1]))
    y = (a[0] * math.sin(a[1]))
    print('Conversion de polares a cartesiano de A')
    return (x, y)


def cartesianob(b):
    x = (b[0] * math.cos(b[1]))
    y = (b[0] * math.sin(b[1]))
    print('Conversion de polares a cartesiano de B')
    return (x, y)


def polar(a):
    p = modulo(a)
    if (a[0] > 0 and a[1] > 0):
        k = math.atan(a[1] / a[0])
    if (a[0] > 0 and a[1] < 0):
        k = 360 - math.atan(a[1] / a[0])
    if (a[0] < 0 and a[1] > 0):
        k = 180 - math.atan(a[1] / a[0])
    if (a[0] < 0 and a[1] < 0):
        k = -180 + math.atan(a[1] / a[0])
    print('Conversion de polares a cartesiano de A')
    return (p, k)


def polarb(b):
    p = modulob(b)
    if (b[0] > 0 and b[1] > 0):
        k = math.atan(b[1] / b[0])
    if (b[0] > 0 and b[1] < 0):
        k = 360 - math.atan(b[1] / b[0])
    if (b[0] < 0 and b[1] > 0):
        k = 180 - math.atan(b[1] / b[0])
    if (b[0] < 0 and b[1] < 0):
        k = -180 + math.atan(b[1] / b[0])
    print('Conversion de polares a cartesiano de B')
    return (p, k)


def SumaVec(d, f):
    MSuma = []
    for i in range(len(d)):
        x = suma(d[i], f[i])
        MSuma.append(x)
    return MSuma


def InverNCom(d):
    for i in range (len(d)):
        d[i] = -d[i]
    return (d)


def MultCom(a, b):
    MMult = []
    for i in range(len(b)):
        x = producto(a, b[i])
        MMult.append(x)
    return (MMult)


def SumMat(a, b):
    Ms = []
    for i in range(len(a)):
        for j in range(len(b)):
            x = suma(a[i][j], b[i][j])
            Ms.append(x)
    return Ms



def MultEscalar(a, b):
    for i in range(len(b)):
        for j in range(len(b)):
            b[i][j] = producto(a, b[i][j])



def conjugadaM(a):
    Matriz = [[(0, 0) for x in a] for x in a[0]]
    for i in range(len(a)):
        for j in range(len(a)):
            Matriz[i][j] = conjugado(a[i][j])
    return Matriz


def TransMat(a):
    Matriz = [[(0,0) for x in a ] for x in a[0]]

    for i in range(len(a[0])):
        for j in range(len(a)):
            Matriz[i][j] = a[j][i]
    return Matriz


def inversamatriz(a):
    for i in range (len(a)):
        a[i] = InverNCom(a[i])
    return a

def AdjuntaMat (a):
    return conjugadaM(TransMat(a))

def ProdMat(a,b):
    if (len(a[0]) != len(b)):
        return "No es posible"
    else:
        matriz = [[(0,0) for x in b[0]] for x in a]
        for i in range (a):
            for j in range (b[0]):
                S = (0,0)
                for w in range (b):
                    S = suma(producto(a[i][w],b[w][j]),S)
                matriz[i][j] = S
        return matriz

def accion (a,b):
    if (len(a[0]) != len(b)):
        return "No es posible completar la operacion"
    else:
        return ProdMat(a,TransMat([b]))

def Dia(a):
    X = (0, 0)
    for i in range(len(a)):
        X = suma(a[j][j], X)
    return X
def ProdInterno(a,b):
    if (len(a[0]) != len(b)):
        return "No es posible"
    else:
        return Dia(ProdMat(AdjuntaMat(a),b))

def Norma(a):
    return math.sqrt(ProdInterno(a, a))

def DistanciaVec(a,b):
    return modulo(resta(b,a))

    
    

