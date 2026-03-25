import time
import subprocess
import os # Necesario para detectar el sistema

def mostrar_menu(op1,op2,op3,op4):
    
    try:
        print("\n--- MENU ---")
        print(f"\n1. {op1} =>")
        print(f"2. {op2} =>")
        print(f"3. {op3} =>")
    except(TypeError,SyntaxError,ValueError):
        print('ingresa lo que quieres mostar en las 4 opciones, con "" ')

# def entervalidation(mensaje):
#         try:
#             num1 = int(input(message))
#             num2 = int(input(mensaje))
#         except ValueError:
#             print("ERROR! enter a correct value. Try again")


def clear():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def write(mensaje):
    for letra in mensaje:
        print(letra, end='', flush=True)
        time.sleep(0.04)
    print()