import math

def temperatura():
    print('''BIENVENIDO A SU CONVERSOR DE TEMPERATURA, ¿QUÉ DESEA HACER?
    1. CELSIUS A FAHRENHEIT
    2. CELSIUS A KELVIN
    3. FAHRENHEIT A CELSIUS 
    4. FARENHEIT A KEVIN
    5. KEVIN A CELSIUS
    6. KEVIN A FAHRENHEIT 
    7. SALIR
    ''')
    op=int(input(' '))
    if op==1:
        c_a_f()
    elif op==2:
        c_a_k()
    elif op==3:
        f_a_c()
    elif op==4:
        f_a_k()
    elif op==5:
        k_a_c()
    elif op==6:
        k_a_f()
    elif op==7:
        print('EL PROGRAMA FINALIZÓ')

def c_a_f():
    celsius=float(input('INGRESE LOS GRADOS CENTIGRADOS: '))
    fahrenheit=celsius*(9/5)+32
    print('Su tempreratura en °F equivale a: ', fahrenheit)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return c_a_f()
    else:
        return temperatura()

def c_a_k():
    celsius=float(input('INGRESE LOS GRADOS CENTIGRADOS: '))
    kelvin=celsius+273.15
    print('Su tempreratura en °K equivale a: ', kelvin)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return c_a_k()
    else:
        return temperatura()

def f_a_c():
    fahrenheit=float(input('INGRESE LOS GRADOS FAHRENHEIT: '))
    celsius=(fahrenheit-32)*(5/9)
    print('Su tempreratura en °C equivale a: ', celsius)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return f_a_c()
    else:
        return temperatura()

def f_a_k():
    fahrenheit=float(input('INGRESE LOS GRADOS FAHRENHEIT: '))
    kelvin=(fahrenheit-32)*(5/9)+273.15
    print('Su tempreratura en °K equivale a: ', kelvin)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return f_a_k()
    else:
        return temperatura()


def k_a_c():
    kelvin=float(input('INGRESE LOS GRADOS KELVIN: '))
    celsius=kelvin-273.15
    print('Su tempreratura en °K equivale a: ', celsius)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return k_a_c()
    else:
        return temperatura()


def k_a_f():
    kelvin=float(input('INGRESE LOS GRADOS KELVIN: '))
    fahrenheit=(kelvin-273.15)*(9/5)+32
    print('Su tempreratura en °F equivale a: ', fahrenheit)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return k_a_f()
    else:
        return temperatura()


a=temperatura()
print(a)  