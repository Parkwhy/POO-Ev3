import os
import time
import DAO.GestionUsuario
import DAO.GestionCliente
from DTO.usuario import usuario
from DTO.Tipo import Tipo_Usuario
from getpass import getpass

def login():
    print("------------------")
    print("      Login       ")
    print("------------------\n")
    print("1- Iniciar Sesion")
    print("2- Registrar Usuario")
    print("3- Salir")
        

def menu_principal():
    os.system('cls')
    print("========== M E N Ú  P R I N C I P A L ==========")
    print("1.- Gestor Clientes")
    print("2.- Gestor Empleados")
    print("3.- Gestor Proyectos")
    print("4.- Gestor Departamentos")
    print("5.- Gestor usuarios")
    print("6.- Salir")
    
def menu_usuarios():
    while True:
        os.system('cls')
        print("========== Menu Usuario ==========")
        print("1.- REGISTRAR USUARIO")
        print("2.- MOSTRAR USUARIOS")
        print("4.- ELIMINAR USUARIO")
        print("5.- SALIR")

        op = int(input("INGRESE OPCIÓN: "))
        if op == 1:
            DAO.GestionUsuario.registrar_usuario()
        elif op == 2:
            opciones_mostrar_usuarios()
        elif op == 3:
            DAO.GestionUsuario.eliminar_usuario()
        elif op == 4:
            print("En desarrollo...")
            time.sleep(2)
        elif op == 5:
            op2 = input("DESEA SALIR [SI/NO]")
            if op2.lower() == "si":
                print(" Adios ")
                time.sleep(2)
                break

def menu_clientes():
    while True:
        os.system('cls')
        print("========== Menu Clientes ==========")
        print("1.- Registrar Cliente")
        print("2.- Mostrar Cliente")
        print("3.- Modificar Cliente")
        print("4.- Eliminar Cliente")
        print("5.- Insertar archivo .JSON")
        print("6.- Salir")

        op = int(input("Ingrese una Opcion: "))
        if op == 1:
            DAO.GestionCliente.registrar_cliente()
        elif op == 2:
            opciones_mostrar_clientes()
        elif op == 3:
            DAO.GestionCliente.modificar_cliente()
        elif op == 4:
            DAO.GestionCliente.eliminar_cliente()
        elif op == 5:
            DAO.GestionCliente.insertar_json()
            time.sleep(2)
        elif op == 6:
            op2 = input("DESEA SALIR [SI/NO]")
            if op2.lower() == "si":
                print(" Adios ")
                time.sleep(2)
                break
            
def opciones_mostrar_usuarios():
    
    op = 0  

    while op != 3:

        
        while True:

            try:
                os.system('cls')
                print("========== Mostrar Usuario ==========")
                print("1.- MOSTRAR TODOS LOS USUARIOS")
                print("2.- MOSTRAR UN USUARIO")
                print("3.- VOLVER AL MENU")
                op = int(input("INGRESE UNA OPCIÓN: "))
                if op == 1:
                    DAO.GestionUsuario.mostrar_usuarios()
                    input("PRESIONA ENTER PARA REGRESAR AL MENU: ")
                    break
                elif op == 2:
                    DAO.GestionUsuario.buscar_usuario() 
                elif op == 3:
                    break
                elif op != 1 and op != 2 and op != 2:
                    print("Saliendo el menu")
                    break
                else:
                    print("¡No existe esa opción! Vuelve a intentar.")
                    time.sleep(1)
                
            except ValueError:
                os.system('cls')
                print("ENTRADA NO VALIDA!")
                print("REDIRECCIONANDO....")
                time.sleep(1)
                
def opciones_mostrar_clientes():
    
        
    while True:
        
        os.system('cls')
        print("========== Mostrar clientes ==========")
        print("1.- mostrar todos los clientes")
        print("2.- mostrar un clientes")
        print("3.- volver al menu")
    
        try:
            opm = int(input("INGRESE UNA OPCIÓN: "))
            if opm == 1:
                DAO.GestionCliente.mostrar_clientes()
                input("PRESIONA ENTER PARA REGRESAR AL MENU: ")
                break
            elif opm == 2:
                DAO.GestionCliente.buscar_cliente() 
            elif opm == 3:
                print("redireccionando")
                time.sleep(0.7)
                break
            else:
                print("¡No existe esa opción! Vuelve a intentar.")
                time.sleep(0.7)
            
        except ValueError:
            print("Entrada no valida, vuelva a intentarlo.")
            time.sleep(1)
                
        
while True:
    os.system('cls')
    login()
    try:
        oplogin = int(input("Ingrese el numero correspondiente a la opcion que desea realizar: "))
        if oplogin == 1:
            while True:
                username = input("Ingrese su usuario : ").lower()
                contra = getpass("Ingrese su contraseña : ").lower()
                credenciales = [username,contra]
                validacion = DAO.GestionUsuario.validacion_usuario(credenciales)
                if validacion == True:
                    print(f"Sesion iniciada correctamente!")
                    print(f"Bienvenido!")
                    time.sleep(2)
                    while(True):
                        try:
                            menu_principal()
                            op = int(input("INGRESE UNA OPCIÓN DEL 1 AL 6: "))
                            if op == 1:
                                menu_clientes()
                            elif op == 2:
                                print("Esta seccion esta en desarrollo...")
                                time.sleep(1)
                            elif op == 3:
                                print("Esta seccion esta en desarrollo...")
                                time.sleep(1)
                            elif op == 4:
                                print("Esta seccion esta en desarrollo...")
                                time.sleep(1)
                            elif op == 5:
                                menu_usuarios()
                            elif op == 6:
                                op2 = int(input("¿DESEA SALIR DEL PROGRAMA? \n Ingrese el numero correspondiente \n 1- si \n 2- no "))
                                if op2 == 1:
                                    print(" Adios ")
                                    time.sleep(2)
                                    exit()
                        except ValueError:
                                print("Entrada no válida. Por favor, ingrese un número del 1 al 6!.")
                                time.sleep(1)
                elif validacion == False:
                    print("Credenciales equivocadas, vuelva a intentar")
                else:
                    time.sleep(1)
                    print("Entrada no valida, vuelva a intentarlo")
                    time.sleep(1)
                    print("Redireccionando..")
                    time.sleep(2)
                    break
        elif oplogin == 2:
            DAO.GestionUsuario.registrar_usuario()
        elif oplogin == 3:
            while True:
                print("¿Deseas salir del programa?")
                print("Seleccione el numero correspondiente.")
                print(" 1-Si \n 2-No")
                salir = int(input("Ingrese una opcion : "))
                if salir == 1:
                    print("Adios!")
                    time.sleep(1)
                    exit()
                elif salir == 2:
                    print("Redireccionando..")
                    time.sleep(1)
                    break
                else:
                    print("Entrada no valida, Vuelva a ingresar una opcion") 
                    time.sleep(1)
                    print("Redireccionando..")
                    time.sleep(0.7) 
                    
                    
    except ValueError:
        print("Entrada no valida, Vuelva a ingresar una opcion") 
        time.sleep(0.7)
        print("Redireccionando..")
        time.sleep(0.7) 
        