#Github
#Readme.md
#Lib.py
#testLib.py
import math

#Empieza la creacion de la libreria
def suma(a,b):
    suma1= a[0] + b[0]
    suma2= a[1] + b[1]
    print('suma')
    return (suma1,suma2)
    

def producto(a,b):
    
    mult=[(a[0]*b[0]),(a[0]*b[1])+(a[1]*b[0]),-(a[1]*b[1])]
    mult1=(mult[0]+mult[2])
    mult2=(mult[1])
    print('producto')
    return (mult1,mult2)


def resta(a,b):
    
    resta1= a[0] - b[0]
    resta2= a[1] - b[1]
    print('Resta')
    return (resta1,resta2)

def division(a,b):
    
    b1=[b[0],-b[1]]
    m=[(a[0]*b1[0]),(a[0]*b1[1])+(a[1]*b1[0]),-(a[1]*b1[1])]
    m1=((b[0]*b1[0])-(b[1]*b1[1]))
    m2=(m[0]+m[2])
    m3=(m[1])
    mResult = m2/m1
    mResult2 = m3/m1
    print('Division')
    return (mResult, mResult2)

def modulo(a):
    x=math.sqrt((a[0]*a[0])+(a[1]*a[1]))
    print('Modulo de a')
    return x

def modulob(b):
    s=math.sqrt((b[0]*b[0])+(b[1]*b[1]))
    print('Modulo de b')
    return s

def conjugado(a):
    con = (a[0],-a[1])
    print('Conjugado de a')
    return (con)

def conjugadob(b):
    con = (b[0],-b[1])
    print('Conjugado de b')
    return (con)

def cartesiano(a):
    x = (a[0]*math.cos(a[1]))
    y = (a[0]*math.sin(a[1]))
    print('Conversion de polares a cartesiano de A')
    return (x,y)

def cartesianob(b):
    x = (b[0]*math.cos(b[1]))
    y = (b[0]*math.sin(b[1]))
    print('Conversion de polares a cartesiano de B')
    return (x,y)

def polar(a):
    p = modulo(a)
    if (a[0]>0 and a[1]>0):
        k = math.atan(a[1]/a[0])
    if (a[0]>0 and a[1]<0):
        k = 360-math.atan(a[1]/a[0])
    if (a[0]<0 and a[1]>0):
        k = 180-math.atan(a[1]/a[0])
    if (a[0]<0 and a[1]<0):
        k = -180+math.atan(a[1]/a[0])
    print('Conversion de polares a cartesiano de A')
    return (p,k)

def polarb(b):
    p = modulob(b)
    if (b[0]>0 and b[1]>0):
        k = math.atan(b[1]/b[0])
    if (b[0]>0 and b[1]<0):
        k = 360-math.atan(b[1]/b[0])
    if (b[0]<0 and b[1]>0):
        k = 180-math.atan(b[1]/b[0])
    if (b[0]<0 and b[1]<0):
        k = -180+math.atan(b[1]/b[0])
    print('Conversion de polares a cartesiano de B')
    return (p,k)
    
    

