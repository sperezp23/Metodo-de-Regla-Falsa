# Metodo de Regla Falsa

# %% Reset
from IPython import get_ipython
get_ipython().magic('reset -sf')

# %% Funciones
import Funciones_Regla_Falsa as f

# %% Entradas
print("\nMetodo de Regla Falsa\n")
Po = float(input("Ingrese el valor de la primera aproximacion(Po)\n"))
P1 = float(input("Ingrese el valor de la segunda aproximacion(P1)\n"))
TOL = float(input("Ingrese el valor de la tolerancia(TOL)\n"))

if TOL != 0.0:
    tipErr = int(input("Escoja el tipo de error, 1:E_abs, 2:E_rel,3:E_%\n"))
else:
    print("\nTipo de error: porcencual")
    
No = int(input("Ingrese el numero maximo de interaciones(No)\n"))
guardar = input("Â¿Quiere guardar el resultado? y/n\n")

# %% Declaracion de variables
i = 2
E = 100.0
alfa = 1.0
epsilon = 6.123233995736766e-17
q0 = f.f(Po)
q1 = f.f(P1)
AproxIni1 = Po
AproxIni2 = P1

# %% Cosideraciones iniciales
if TOL == 0.0:
    TOL = epsilon
    tipErr = 3

if tipErr < 1.0 or tipErr > 3.0:
    tipErr = 2

#Tipo de error(Mensaje)    
if tipErr == 1:
    Err = "_abs"
elif tipErr == 2:
    Err = "_rel"
elif tipErr == 3:
    Err = "_%"
    
# %% Metodo de Regla Falsa
while E> epsilon and i<=No:
    p = P1 - (q1*((P1-Po)/(q1-q0)))
    q = f.f(p)
    
    if p != 0.0:
        E = f.Errores(tipErr,p,P1)
    
    delta = abs(p-P1)
    alfa = abs(E/alfa)
    
    #Impresion y almacenamiento de resultados
    if abs(p-P1) < TOL:
        print("-------------------------------------------------------------")
        print("Proceso exitoso")
        print("Po =",AproxIni1)
        print("P1 =",AproxIni2)
        print("p =",p)
        print("f(p) =",f.f(p))
        print("Error"+Err+" =",E)
        print("Alfa =",alfa)
        print("Delta =",delta)
        print("TOL =",TOL)
        print("No =",i)
        print("-------------------------------------------------------------")
        
        #Archivo de texto con los datos
        if guardar == "y":        
            resultado_ReglaFalsa = open("resultado_Regla_Falsa.txt","a")
            resultado_ReglaFalsa.write("Po = "+str(AproxIni1)+"\n")
            resultado_ReglaFalsa.write("P1 = "+str(AproxIni2)+"\n")
            resultado_ReglaFalsa.write("p = "+str(p)+"\n")
            resultado_ReglaFalsa.write("Error"+Err+" = "+str(E)+"\n")
            resultado_ReglaFalsa.write("Alfa = "+str(alfa)+"\n")
            resultado_ReglaFalsa.write("Delta = "+str(delta)+"\n")
            resultado_ReglaFalsa.write("TOL = "+str(TOL)+"\n")
            resultado_ReglaFalsa.write("No = "+str(i)+"\n")
            resultado_ReglaFalsa.write("-------------------------------------------------------------\n")
            resultado_ReglaFalsa.close()
        break
            
    if q*q1 < 0:
        Po = P1
        q0 = q1
    
    i += 1
    P1 = p
    q1 = q
    alfa = E
    
if i > No:
    print("\nEl metodo ha fallado luego de la interación No =", i+1)        