import math

def tiempo():
    print('''BIENVENIDO A SU CONVERSOR DE VELOCIDAD, ¿QUÉ DESEA HACER?
    1. METROS/SEGUNDOS A KILOMETROS/HORA
    2. KILOMETROS/HORA A METROS/SEGUNDO
    3: SALIR
    ''')
    op=int(input(' '))
    if op==1:
        ms_a_kh()
    elif op==2:
        kh_a_ms()
    elif op==3:
        print('EL PROGRAMA FINALIZÓ')   
def ms_a_kh():
    ms=float(input('INGRESE LOS METROS/SEGUNDOS: '))
    kh=ms*3.6
    print('Sus metros/segundos a kilometros/hora equivale a: ', kh)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return ms_a_kh()
    else:
        return tiempo()

def kh_a_ms():
    kh=float(input('INGRESE LOS METROS/SEGUNDO: '))
    ms=kh/3.6
    print('Sus kilometros/metros a metros/segundo equivale a: ', ms)
    op=int(input('''¿DESEA CONVERTIR MÁS DATOS?
    1. Si
    2. NO
    '''))
    if op==1:
        return kh_a_ms()
    else:
        return tiempo()

a=tiempo()
print(a)  