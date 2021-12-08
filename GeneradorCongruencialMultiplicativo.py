a = int(input("Ingrese el valor del constante multiplicativo:\n"))
a = round(a)
if 0>=a : #this is used to avoid any problems
    while True:
        a = int(input("Por favor ingrese un valor válido:\n"))
        a = round(a)
        if(0<a):
            break

xo = int(input("Ingrese el valor de la semilla inicial:\n"))
xo = round(xo)
if 0>=xo  : #this is used to avoid any problems
    while True:
        xo = int(input("Por favor ingrese un valor válido:\n"))
        xo = round(xo)
        if(0<xo):
            break

m = int(input("Ingrese el valor del módulo:\n"))
m = round(m)
if 0>=m  : #this is used to avoid any problems
    while True:
        m = int(input("Por favor ingrese un valor válido:\n"))
        m = round(m)
        if(0<m):
            break
pe=0
result=0
i=0
while result != m:

    if(2**i == m):
        if(i<=5):
            pe=(m/4)
            result = m
        else:
            if(i==0):
                pe=1
                result = m
            if(i==1):
                pe=2
                result = m
            else:
                pe=(2**i-2)
                result = m
    if(10**i == m):
        if(i<=5):
            pe=(5*(10**(i-2)))
            result = m
        else:
            pe=((5**(i-1))*4)
            result = m
    i=i+1

newx0=xo
axomodm=0
i=0

while axomodm !=xo or i < pe:
    axomodm=((a*newx0)%m)
    newx0=axomodm
    i += 1
if(axomodm==xo and i==(pe)):
    print("Generador congruencial multiplicativo confiable/Generador con periodo completo.")
else:
    print("Generador congruencial multiplicativo no confiable/Generador con periodo incompleto.")