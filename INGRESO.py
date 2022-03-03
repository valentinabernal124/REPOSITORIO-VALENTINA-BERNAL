

def ingreso():
    print('BIENVENIDO, ¿QUÉ DESEA HACER?')
    op=int(input('''1. CONVERTIR TEMPERATURAS
2. CONVERTIR VOLUMENES
3. CONVERTIR VELOCIDADES
4. salir
'''))
    if op==1:
        from TEMPERATURA import temperatura
        print(temperatura)
    elif op==2:
        from VOLUMEN import volumen
        print(volumen)
    elif op==3:
        from VELOCIDAD import tiempo
        print(tiempo)
a=ingreso()
print(ingreso)


