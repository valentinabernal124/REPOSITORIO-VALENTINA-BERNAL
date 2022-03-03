import math

def volumen():
    print('''BIENVENIDO A SU CONVERSOR DE VOLUMEN, ¿QUÉ DESEA HACER?
    1. LITROS A MILILITROS
    2. LITROS A METROS CÚBICOS
    3. MILILITROS A LITROS
    4. MILILITROS A METROS CÚBICOS 
    5. METROS CÚBICOS A LITROS
    6. METROS CÚBICOS A MILILITROS
    7. SALIR
    ''')
    op=int(input(' '))
    if op==1:
        l_a_ml()
    elif op==2:
        l_a_mc()
    elif op==3:
        ml_a_l()
    elif op==4:
        ml_a_mc()
    elif op==5:
        mc_a_l()
    elif op==6:
        mc_a_ml()

def l_a_ml():
    litros=float(input('INGRESE LOS LITROS: '))
    mililitros=litros*1000
    print('Su valor de litros a mililitros equivale a: ', mililitros)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return l_a_ml()
    else:
        return volumen()


def l_a_mc():
    litros=float(input('INGRESE LOS LITROS: '))
    metroscubicos=litros/1000
    print('Su valor de litros a mililitros equivale a: ', metroscubicos)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return l_a_mc()
    else:
        return volumen()


def ml_a_l():
    mililitros=float(input('INGRESE LOS MILILITROS: '))
    litros=mililitros/1000
    print('Su valor de mililitros a litros equivale a: ', litros)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return ml_a_l()
    else:
        return volumen()


def ml_a_mc():
    mililitros=float(input('INGRESE LOS MILILITROS: '))
    metroscubicos=(mililitros)/(10^6) 
    print('Su valor de mililitros a litros equivale a: ', metroscubicos)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return ml_a_mc()
    else:
        return volumen()


def mc_a_l():
    metroscubicos=float(input('INGRESE LOS METROS CÚBICOS: '))
    litros=metroscubicos*1000
    print('Su valor de metros cúbicos a litros equivale a: ', litros)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return mc_a_l()
    else:
        return volumen()


def mc_a_ml():
    metroscubicos=float(input('INGRESE LOS MILILITROS: '))
    mililitros=metroscubicos*(10^6) 
    print('Su valor de metros cúbicos a mililitros equivale a: ', mililitros)

    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return mc_a_ml()
    else:
        return volumen()



a=volumen()
print(a)  
      





