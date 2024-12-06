import time
import os
import re
from DTO.usuario import usuario
from DAO.Conexion import Conexion
from getpass import getpass
import bcrypt

conexion = Conexion(
    host='localhost',
    user='userempresa',
    password='V3ntana.13',
    db='empresa')
    
    
def registrar_usuario():
    os.system('cls')
    print("========== Registrar Usuario ==========")
    
    
    username = input("INGRESE SU USUARIO: \n DEBE TENER ENTRE 5 Y 20 CARACTERES \n : ").lower()
    
    while True:
        
        while len(username) < 5 or len(username) > 20:
            print("SU USUARIO DEBE TENER ENTRE 5 Y 20 CARACTERES!")
            username = input("INGRESE SU USUARIO: \n DEBE TENER ENTRE 5 Y 20 CARACTERES \n : ").lower()
        
        credenciales = username
        credenciales = validacion_usuario_existente(credenciales)
        if credenciales == True:
            print("El usuario ya existe, porfavor ingrese uno distinto.")
            print("SU USUARIO DEBE TENER ENTRE 5 Y 20 CARACTERES!")
            username = input("INGRESE SU USUARIO: \n DEBE TENER ENTRE 5 Y 20 CARACTERES \n : ").lower()
        else:
            break
        
    

    
    nombre = input("INGRESE SOLO SU PRIMER NOMBRE: ").capitalize()
    
    while nombre.isalpha() == False or len(nombre) > 40:
        print("SU NOMBRE NO DEBE TENER ESPACIO NI DIGITOS Y PUEDE TENER UN MAXIMO 40 CARACTERES!")
        nombre = input("INGRESE SOLO SU PRIMER NOMBRE: ").capitalize()
        
        
    apellido = input("INGRESE SOLO SU PRIMER APELLIDO: ").capitalize()
    
    while apellido.isalpha() == False or len(apellido) > 40:
        print("SU APELLIDO NO DEBE TENER ESPACIO NI DIGITOS Y PUEDE TENER UN MAXIMO 40 CARACTERES!")
        apellido = input("INGRESE SOLO SU PRIMER APELLIDO: ").capitalize()
        
        
    correo = input("Ej: Correo@empresa.dominio \n INGRESE SU CORREO:")
    
    while validar_correo(correo) == False:
        print("CORREO NO VALIDO")
        correo=input("Ej: Correo@empresa.dominio \n INGRESE SU CORREO:")
        
        
    telefono = input("INGRESE SU TELEFONO +56 9: ")
    
    while telefono.isdigit() == False or len(telefono) > 8 or len(telefono) < 8:
        print("PORFAVOR INGRESE UN NUMERO VALIDO")
        telefono = input("INGRESE SU TELEFONO +56 9: ")
        
    
        
    while True:   
        clave = getpass("LA CONTRASEÑA DEBE TENER MINIMO 6 CARACTERES Y MAXIMO 10! \n INGRESE SU CONTRASEÑA: ").lower()
        
        while len(clave) < 6 or len(clave) > 10:
            print("LA CONTRASEÑA DEBE TENER MINIMO 6 CARACTERES Y MAXIMO 10!")
            clave = getpass("INGRESE SU CONTRASEÑA: ").lower()
            
        clave2 = getpass("REPITA LA CONTRASEÑA: ").lower()
        if clave == clave2:
            print("Contraseña correcta!")
            time.sleep(1)
            break
        else:
            print("Las contraseñas no coinciden, vuelva a intentarlo")
            time.sleep(1)
    
    
    while True:
        tipo = int(input("""Seleccione el numero correspondiente al rol de usuario que desea tener
                        1 -Vendedor
                        2 -Administrador \n -> """))
        
        if tipo == 1:
            tipo = "Vendedor"
            break
        elif tipo == 2:
            tipo = "Administrador"
            break
        else:
            print("Error en la asignacion de roles")
    
    clave = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())
    
    u = usuario(nombre, apellido, correo, telefono, clave, tipo, username)
   #id	nombre	apellido	correo	telefono	clave	tipo	username
    sql = f"""INSERT INTO usuario (nombre, apellido, correo, telefono, clave, tipo, username)
        VALUES ('{u.nombre}', '{u.apellido}', '{u.correo}', '{u.telefono}', '{u.clave.decode('utf-8')}', '{u.tipo}', '{u.username}')"""

    conexion.ejecuta_query(sql)
    conexion.commit()
    input("\n datos ingresados Satisfactoriamente, presione ENTER para continuar!")
    

def mostrar_usuarios(): #	id	nombre	apellido	correo	telefono	clave	tipo	username	
    try:
        sql = "select * from usuario "
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchall()
        os.system('cls')
        print("========== Listado de Usuarios ==========")
        for dato in datos:
            print(f"ID {dato[0]} - NOMBRE: {dato[1]} - APELLIDO: {dato[2]} - Correo: {dato[3]} - Telefono: {dato[4]} - tipo usuario: {dato[6]} - username: {dato[7]}")
            print("--------------------------------------------")
            
    except:
        conexion.rollback


def mostrar_usuarios_pacial(): #Muestra solo algunos datos para la funcion "buscar_usuario()"
    try:
        sql = "select * from usuario "
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchall()
        os.system('cls')
        print("========== Listado de Usuarios ==========")
        for dato in datos:
            print(f"ID {dato[0]} - NOMBRE: {dato[1]} - APELLIDO: {dato[2]} - Username: {dato[7]}")
            print("--------------------------------------------")
    except:
        conexion.rollback
        

def buscar_usuario(): #id	nombre	apellido	correo	telefono	clave	tipo	username
    
    while True:
        
        os.system('cls')
        mostrar_usuarios_pacial()
        try:
            print("========== MUESTRA DE DATOS PARTICULAR ==========")
            op = int(input("Ingrese valor del ID del Usuario que desea mostrar los datos: "))


            sql=f"select * from usuario where id={op}"
            cursor=conexion.ejecuta_query(sql)
            datos=cursor.fetchone()

            if datos is None : 
                print("No hay usuarios registrados, ingrese un nuevo usuario")
                time.sleep(2)
            else:
                break
                #id	nombre	apellido	correo	telefono	clave	tipo	 username	
        except ValueError:
                print("ENTRADA NO VALIDA!")
                print("REDIRECCIONANDO....")
                time.sleep(0.7)
    print("\n==========================================")
    print("MUESTRA DE DATOS DEL USUARIO")
    print("==========================================")
    print(f" ID: {datos[0]}")
    print(f" nombre: {datos[1]}")
    print(f" apellido: {datos[2]}")
    print(f" correo: {datos[3]}")
    print(f" Telefono: +56 9 {datos[4]}")
    print(f" tipo: {datos[6]}")
    print(f" username: {datos[7]}")
    
    input("\n Ingresa ENTER para continuar.")


def eliminar_usuario():
    while True:
        
        os.system('cls')
        print("========== OPCIÓN ELIMINAR USUARIO ==========")
        mostrar_usuarios()
        
        try:
            op = int(input("Desea eliminar un usuario? Seleccione el numero correspondiente \n 1- Si \n 2- No \n -> "))
            
            if op == 1:
                try:
                    id = int(input("Ingrese valor de ID del Usuario que desea eliminar: "))
                    
                    sql_verificador = f"SELECT * FROM usuario WHERE id = {id}"
                    cursor = conexion.ejecuta_query(sql_verificador)
                    usuario = cursor.fetchone()
                    
                    if usuario is None:
                        print(f"El ID {id} no existe. ingrese un ID válido.")
                        time.sleep(2)
                    elif usuario != None:
                        sql = f"DELETE FROM usuario WHERE id = {id}"
                        conexion.ejecuta_query(sql)
                        conexion.commit()
                        print("Usuario eliminado")
                        input("Presione ENTER para continuar.")
                        break
                    else:
                        print("Seleccione un id valido")
                        time.sleep(0.8)        
                except (ValueError, Exception):
                    conexion.rollback()
                    print("Ingrese un ID valido")
                    time.sleep(2)
            elif op == 2:
                print("Redirigiendo...")
                time.sleep(0.8)
                break
            else:
                print("Seleccione una opcion valida")
                time.sleep(0.8)
        except ValueError:
            print("Seleccione una opcion valida")
            time.sleep(0.8)
            
       
def validar_correo(correo):
    estructura = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if re.match(estructura,correo):
        return True
    else:
        return False
    
def validacion_usuario(credenciales): #Desarrollar
    try: 
        sql = f"SELECT * FROM usuario WHERE username = '{credenciales[0]}'"
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchone()
        
        
        
        if datos != None:
            hashed_password = datos[5].encode('utf-8')  
            
            if bcrypt.checkpw(credenciales[1].encode('utf-8'), hashed_password):
                return True
            else:
                return False 
            
        else:
            return False  
        
    except Exception as e:
        print(f"Error en la validación del usuario: {e}")
        conexion.rollback()
        
def validacion_usuario_existente(credenciales):
    try: 
        sql = f"SELECT * FROM usuario WHERE username = '{credenciales}'"
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchone()
        
        if datos is None:
            return False
        
        elif credenciales == datos[7]:
            return True
        else:
            return False
    
    except Exception as e:
        print(e)
        conexion.rollback()
    
    