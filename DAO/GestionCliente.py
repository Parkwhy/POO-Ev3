import time
import os
from DTO.Cliente import Cliente
from DAO.Conexion import Conexion
import re
from getpass import getpass
import mysql.connector
import requests

conexion = Conexion(
    host='localhost',
    user='userempresa',
    password='V3ntana.13',
    db='empresa')
    
    
def registrar_cliente():
    os.system('cls')
    print("========== Registrar Cliente ==========")
    #run, nombre, apellido, direccion, fono, correo, tipo, montoCredito=500, deuda=0
    
    
    while True: 
        
        run = input("Ingrese su rut con el siguente formato: \n EJ: 21253051-7: ")
        
        if validar_rut(run) == False:
            print("Su rut debe contener digito, guion y tener una longitud de entre 9 y 10 caracteres. NO DEBE TENER PUNTOS NI ESPACIOS \n Ej: 21253051-7 ")
            run = input("Ingrese su RUT en el formato mostrado: ")
        if validacion_rut_cliente(run) == True:
            print("El rut ya existe, ingrese uno distinto")
        else:
            print("Rut ingresado correctamente.")
            break    
        
        
    nombre = input("INGRESE SOLO SU PRIMER NOMBRE: ").capitalize()
    
    while nombre.isalpha() == False or len(nombre) > 40:
        print("SU NOMBRE NO DEBE TENER ESPACIO NI DIGITOS Y PUEDE TENER UN MAXIMO 40 CARACTERES!")
        nombre = input("INGRESE SOLO SU PRIMER NOMBRE: ").capitalize()
        
  
    apellido = input("INGRESE SOLO SU PRIMER APELLIDO: ").capitalize()
    
    while apellido.isalpha() == False or len(apellido) > 40:
        print("SU APELLIDO NO DEBE TENER ESPACIO NI DIGITOS Y PUEDE TENER UN MAXIMO 40 CARACTERES!")
        apellido = input("INGRESE SOLO SU PRIMER APELLIDO: ").capitalize()
       
    direccion = input("INGRESE SU DIRECCION : ").lower()
    
    while len(direccion) < 5 or len(direccion) > 100:
        print("PORFAVOR INGRESE UNA DIRECCION VALIDA")
        direccion = input("INGRESE SU DIRECCION: ").lower()
        

    fono = input("INGRESE SU TELEFONO +56 9: ")
    
    while fono.isdigit() == False or len(fono) != 8:
        print("PORFAVOR INGRESE UN NUMERO VALIDO, debe tener 8 digitos.")
        fono = input("INGRESE SU TELEFONO +56 9: ")
        
        
    correo = input("Ej: Correo@empresa.dominio \n INGRESE SU CORREO:")
    
    while validar_correo(correo) == False:
        print("CORREO NO VALIDO")
        correo=input("Ej: Correo@empresa.dominio \n INGRESE SU CORREO:")
        
        
    while True:
        
        tipos_usuario()
        
        tipo = int(input("""Seleccione el numero correspondiente al rol de usuario que desea tener \n -> """))
        
        if tipo == 1:
            tipo = "Bronze" 		  
            break
        elif tipo == 2:
            tipo = "Silver"
            break
        if tipo == 3:
            tipo = "Gold" 		  
            break
        elif tipo == 4:
            tipo = "Platinum"
            break
        else:
            print("Error en la asignacion de roles")
            
                        

    while True:
        try:
            montoCredito = int(input("INGRESE SU CREDITO"))
            if montoCredito >= 0 :
                break
            elif montoCredito < 0:
                    print("Debes ingresar un credito mayor o igual que 0")
        except ValueError:
            print("PORFAVOR INGRESE UN NUMERO VALIDO")
      
    
    while True:
        try:
            deuda = int(input("INGRESE SU DEUDA :"))
            if deuda >= 0 :
                break
            elif deuda < 0:
                print("Debes ingresar una deuda mayor o igual que 0")
        except ValueError:
            print("PORFAVOR INGRESE UN NUMERO VALIDO")

    
    #run, nombre, apellido, direccion, fono, correo, tipo, montoCredito=500, deuda=0
    c = Cliente(run,nombre,apellido,direccion,fono,correo,tipo,montoCredito,deuda)
  
    sql = f"""INSERT INTO cliente (rut, nombre, apellido, direccion, fono, tipo, montoCredito, deuda)
        VALUES ('{c.run}', '{c.nombre}', '{c.apellido}', '{c.direccion}', '{c.fono}', '{c.tipo}', '{c.montoCredito}', {c.deuda})"""

    conexion.ejecuta_query(sql)
    conexion.commit()
    input("\n datos ingresados Satisfactoriamente, presione ENTER para continuar!")
    

def mostrar_clientes(): #run, nombre, apellido, direccion, fono, correo, tipo, montoCredito=500, deuda=0
    try:
        sql = "select * from cliente"
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchall()
        os.system('cls')
        
        if datos == None or len(datos) == 0:
            print("No hay clientes registrados en el sistema.")
        elif datos != None:
            print("========== Listado de Clientes ==========")
            for dato in datos:
                print(f"ID {dato[0]} - run: {dato[1]} - apellido: {dato[2]} - direccion: {dato[3]} - fono: {dato[4]} - correo: {dato[5]} - tipo: {dato[7]} - montoCredito: {dato[8]} - deuda: {dato[9]}")
                print("--------------------------------------------")
        else:
            print("Error, redireccionando")
            time.sleep(0.8)
        
    except:
        conexion.rollback


def mostrar_clientes_pacial(): #no se esta usando
    try:
        sql = "select * from cliente "
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchall()
        os.system('cls')
        
        
        if datos == None or len(datos) == 0:
            input("Lamentablemente no hay clientes registrados. \n Presione Enter para continuar")
        elif datos != None:

            print("========== Listado de clientes ==========")
            for dato in datos:
                print(f"ID {dato[0]} - Run: {dato[1]} - Nombre: {dato[2]} - Apellido: {dato[3]}")
                print("--------------------------------------------")
        else:
            print("Error, redireccionando")
            time.sleep(0.8)
    except:
        conexion.rollback
        

def buscar_cliente():
    
    while True:
        
        os.system('cls')
        mostrar_clientes_pacial()
        
        
        op1 = int(input("Que operacion desea realizar? Seleccione el numero correspondiente. \n 1- Consultar cliente \n 2- Volver al menu \n -> "))
        
        if op1 == 1:
            print("========== MUESTRA DE DATOS PARTICULAR ==========")
            op = int(input("Ingrese el ID del Cliente que desea mostrar los datos: "))


            sql=f"select * from cliente where id={op}"
            cursor=conexion.ejecuta_query(sql)
            datos=cursor.fetchone()

            print (datos)
            print("buscar_cliente")
            
            if datos is None or len(datos) == 0: 
                print("No existe ese cliente, ingrese un nuevo cliente")
                time.sleep(2)
            elif datos != None :
                print("\n==========================================")
                print("MUESTRA DE DATOS DEL CLIENTE")
                print("==========================================")
                print(f" ID: {datos[0]}")
                print(f" run: {datos[1]}")
                print(f" apellido: {datos[2]}")
                print(f" direccion: {datos[3]}")
                print(f" fono: {datos[4]}")
                print(f" correo: {datos[5]}")
                print(f" tipo: +56 9 {datos[6]}")
                print(f" montoCredito: {datos[7]}")
                print(f" deuda: {datos[8]}")
            else:
                input("Error en la consulta de clientes. Volviendo")
        elif op1 == 2:
            print("Seguro desea volver al menu?")
            op2 = int(input("Seleccione un numero \n 1- Si \n 2- No"))
            if op2 == 1:
                print("Redireccionando al menu")
                time.sleep(0.7)
                break
            if op2 == 2:
                print("Volviendo")
                
            else:
                print("Seleccione una opcion valida.")
            
        else:
            print("Porfavor Seleccione una opcion valida.")

#run, nombre, apellido, direccion, fono, correo, tipo, montoCredito=500, deuda=0

def modificar_cliente(): #run, nombre, apellido, direccion, fono, correo, tipo, montoCredito=500, deuda=0 
    os.system('cls')
    lista_nuevos = []
    print("========== MODIFICAR DATOS DE CLIENTE ==========")
    mostrar_clientes()
    while True:
        try:
            modif = int(input("Desea realizar una modificacion? \n 1- Si \n 2-No : "))
            if modif == 1:
                op = int(input("\n Ingrese valor de ID del Cliente que desea modificar: "))
                validacion = validacion_cliente(op)
                if validacion == False:
                    print("El usuario no existe, seleccione un usuario existente")
                    continue
                try:
                    sql=f"select * from cliente where id={op}"
                    cursor=conexion.ejecuta_query(sql)
                    datos=cursor.fetchone()
                except Exception as e:
                    conexion.rollback()
                    print("Se produjo el error ",e)
                    
                datos_actuales = datos
                
                print(f" ID: {datos_actuales[0]} RUT: {datos_actuales[1]}")
                lista_nuevos.append(datos_actuales[0])
                lista_nuevos.append(datos_actuales[1])
                try:
                    op2 = int(input(f"DESEA MODIFICAR EL NOMBRE?: {datos_actuales[2]} - 1-SI 2-NO: "))
                    if op2 == 1:
                        nombre_nuevo = input("INGRESE NOMBRE: ")
                        
                        while nombre_nuevo.isalpha() == False or len(nombre_nuevo) > 40:
                            print("Su nombre no puede tener caracteres mas de 40 caracteres y estos deben ser letras")
                            nombre_nuevo = input("INGRESE SU NOMBRE: ")
                        
                        lista_nuevos.append(nombre_nuevo)
                    elif op2 == 2:
                        print("Se mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[2])
                    else:
                        print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[2])
                except:
                    print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                    lista_nuevos.append(datos_actuales[2])
        
                try:
                    op2 = int(input(f"DESEA MODIFICAR EL APELLIDO?: {datos_actuales[3]} - 1-SI 2-NO: : "))
                    if op2 == 1:
                        
                        apellido_nuevo = input("INGRESE APELLIDO: ")
                        while apellido_nuevo.isalpha() == False or len(apellido_nuevo) > 40:
                            print("Su apellido no puede tener caracteres mas de 40 caracteres y estos deben ser letras")
                            apellido_nuevo = input("INGRESE SU APELLIDO: ")
                    
                        lista_nuevos.append(apellido_nuevo)
                    elif op2 == 2:
                        print("Se mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[3])
                    else:
                        print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[3])
                except:
                    print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                    lista_nuevos.append(datos_actuales[3])
                
                
                #Aqui va direccion
                try:
                    op2 = int(input(f"DESEA MODIFICAR EL DIRECCION?: {datos_actuales[4]} - 1-SI 2-NO: : "))
                    if op2 == 1:
                        
                        direccion_nueva = input("INGRESE SU DIRECCION: ").lower()
                        
                        
                        while len(direccion_nueva) < 5 or len(direccion_nueva) > 100:
                            print("PORFAVOR INGRESE UNA DIRECCION VALIDA")
                            direccion_nueva = input("INGRESE SU DIRECCION: ").lower()
                        
                        lista_nuevos.append(direccion_nueva)
                    elif op2 == 2:
                        print("Se mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[4])
                    else:
                        print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[4])
                except:
                    print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                    lista_nuevos.append(datos_actuales[4])
                #aqui va direccion .fin
                try:
                    op2 = int(input(f"DESEA MODIFICAR EL TELEFONO?: {datos_actuales[5]} - 1-SI 2-NO: : "))
                    if op2 == 1:
                        fono = input("INGRESE SU TELEFONO +56 9: ")
                        
                        while fono.isdigit() == False or len(fono) != 8:
                            print("PORFAVOR INGRESE UN NUMERO VALIDO, debe tener 8 digitos.")
                            fono = input("INGRESE SU TELEFONO +56 9: ")
                        lista_nuevos.append(fono)
                    elif op2 == 2:
                        print("Se mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[5])
                    else:
                        print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[5])
                except:
                    print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                    lista_nuevos.append(datos_actuales[5])
                
                
                try:
                    op2 = int(input(f"DESEA MODIFICAR EL CORREO?: {datos_actuales[6]} - 1-SI 2-NO: : "))
                    if op2 == 1:
                        correo_nuevo = input("INGRESE UN CORREO: ")
                        
                        
                        while validar_correo(correo_nuevo) == False:
                            print("Correo no valido.")
                            correo_nuevo = input("INGRESE SU CORREO: ")
                            
                        lista_nuevos.append(correo_nuevo)
                        
                    elif op2 == 2:
                        print("Se mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[6])
                    else:
                        print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[6])
                except:
                    print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                    lista_nuevos.append(datos_actuales[6])
                
                #aqui va tipo
                try:
                    op2 = int(input(f"DESEA MODIFICAR SU TIPO?: {datos_actuales[7]} - 1-SI 2-NO: : "))

                    if op2 == 1:
                        while True:
                            
                            tipos_usuario()
                            
                            tipo = int(input("""Seleccione el numero correspondiente al rol de usuario que desea tener \n -> """))
                            
                            if tipo == 1:
                                tipo_nuevo = "Bronze" 		  
                                break
                            elif tipo == 2:
                                tipo_nuevo = "Silver"
                                break
                            if tipo == 3:
                                tipo_nuevo = "Gold" 		  
                                break
                            elif tipo == 4:
                                tipo_nuevo = "Platinum"
                                break
                            else:
                                print("Error en la asignacion de roles")
                        lista_nuevos.append(tipo_nuevo)

                    elif op2 == 2:
                        print("Se mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[7])
                    else:
                        print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[7])
                except:
                    print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                    lista_nuevos.append(datos_actuales[7])
                 
                try:   
                    op2 = int(input(f"DESEA MODIFICAR EL monto de su credito?: {datos_actuales[8]} - 1-SI 2-NO : "))
                    if op2 == 1:
                        while True:
                            try:
                                montoCredito_nuevo = int(input("INGRESE SU CREDITO"))
                                if montoCredito_nuevo >= 0 :
                                    break
                                elif montoCredito_nuevo < 0:
                                        print("Debes ingresar un credito mayor o igual que 0")
                            except ValueError:
                                print("PORFAVOR INGRESE UN NUMERO VALIDO")
                                continue
                        
                            lista_nuevos.append(montoCredito_nuevo)
                            break
                    elif op2 == 2:
                        print("Se mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[8])
                    else:
                        print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[8])
                except:
                    print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                    lista_nuevos.append(datos_actuales[8])
                
                try:  
                    op2 = int(input(f"DESEA MODIFICAR SU DEUDA?: {datos_actuales[9]} - 1-SI 2-NO : "))
                    if op2 == 1:
                        while True:
                            try:
                                deuda_nueva = int(input("INGRESE SU DEUDA :"))
                                if deuda_nueva >= 0 :
                                    break
                                elif deuda_nueva < 0:
                                    print("Debes ingresar una deuda mayor o igual que 0")
                            except ValueError:
                                print("PORFAVOR INGRESE UN NUMERO VALIDO")
                        
                        lista_nuevos.append(deuda_nueva)
                        break
                    elif op2 == 2:
                        print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                        lista_nuevos.append(datos_actuales[9])
                    else:
                        print("Seleccione una opcion valida")
                except:
                    print("No se selecciono una opcion valida, mantendran los datos anteriores.")
                    lista_nuevos.append(datos_actuales[9])
                        
                        


                try: #run, nombre, apellido, direccion, fono, correo, tipo, montoCredito=500, deuda=0
                    sql = f"UPDATE cliente SET nombre='{lista_nuevos[2]}', apellido='{lista_nuevos[3]}', direccion='{lista_nuevos[4]}', fono={lista_nuevos[5]}, correo='{lista_nuevos[6]}', tipo='{lista_nuevos[7]}', montoCredito={lista_nuevos[8]}, deuda={lista_nuevos[9]} WHERE id={lista_nuevos[0]}"

                    conexion.ejecuta_query(sql)
                    conexion.commit()
                    print("Datos modificados satisfactoreamente!")
                    input("PRESIONE ENTER PARA SALIR: ")
                    
                except Exception as e:
                    conexion.rollback()
                    print("Se produjo el error ",e)
            elif modif == 2:
                break
            else:
                print("Seleccione una opcion valida")
                    
        except ValueError:
            print("Ingrese un valor valido")
            continue
    


def eliminar_cliente():
    while True:
        print("========== MENU ELIMINAR CLIENTE ==========")
        mostrar_clientes()
        
        try:
            op = int(input("Desea eliminar un cliente? Seleccione el numero correspondiente \n 1- Si \n 2- No \n -> "))
            if op == 1:
                try:
                    id = int(input("Ingrese el id del cliente que desea eliminar: "))
                    
                    sql_verificador = f"SELECT * FROM cliente WHERE id = {id}"
                    cursor = conexion.ejecuta_query(sql_verificador)
                    cliente = cursor.fetchone()
                    
                    if cliente is None:
                        print(f"El usuario {id} no existe. ingrese un id válido.")
                        time.sleep(2)
                        continue
                    
                    sql = f"DELETE FROM cliente WHERE id = {id}"
                    conexion.ejecuta_query(sql)
                    conexion.commit()
                    print("cliente eliminado")
                    input("Presione ENTER para continuar.")
                    break
                
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

def validar_rut(run):
    estructura = r"^[0-9]{7,8}-[0-9kK]$"
    
    if re.match(estructura,run):
        return True
    else:
        return False
    
def validacion_rut_cliente(validacion): #Desarrollar
    try: 
        sql = f"SELECT * FROM cliente WHERE rut = '{validacion}'"
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchone()
        
        if datos == None:
            return False
        elif validacion in datos:
            return True
        elif validacion not in datos: 
            return False
        else:
            return False
        
    except Exception as e:
        print(e)
        conexion.rollback()
        
def validacion_cliente(validacion): #Desarrollar
    try: 
        sql = f"SELECT * FROM cliente WHERE id = '{validacion}'"
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchone()
        
        if datos == None:
            return False
        elif validacion in datos:
            return True
        elif validacion not in datos: 
            return False
        else:
            return False
        
    except Exception as e:
        print(e)
        conexion.rollback()
        
def validacion_Json(rut):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='userempresa',
            password='V3ntana.13',
            db='empresa'
        )
        cursor = conexion.cursor()

        sql = "SELECT * FROM cliente WHERE rut = %s"
        cursor.execute(sql, (rut,)) 
        datos = cursor.fetchone()

        if datos is None:
            return False  
        else:
            return True  
    except Exception as e:
        print(f"Error al validar el cliente: {e}")
        conexion.rollback()
        return False
    finally:
        if cursor:
            cursor.close()  
        if conexion:
            conexion.close()


    
def tipos_usuario():

    try: 
        sql = f"SELECT * FROM tipo"
        cursor = conexion.ejecuta_query(sql)
        datos = cursor.fetchall()

        
        for dato in datos:
            print(f"ID : {dato[0]} Tipo : {dato[1]} ")
            
    except Exception as e:
        print(e)
        conexion.rollback()
    
    
import mysql.connector
import requests

def obtener_datos_desde_api():
    url = "https://raw.githubusercontent.com/Parkwhy/POO-Ev3/refs/heads/master/Json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as error:
        print("Error al hacer la solicitud:", error)
        return None

def insertar_json():
    data = obtener_datos_desde_api()
    

    if not data:
        print("No se obtuvieron datos desde la API.")
        return

    print(data)  # Asegúrate de que los datos se están imprimiendo correctamente
    time.sleep(0.8)
    
    conexion = mysql.connector.connect(
        host='localhost',
        user='userempresa',
        password='V3ntana.13',
        db='empresa'
    )
    cursor = conexion.cursor()

   
    for item in data:
        rut = item['rut']  
        
       
        vali_client = validacion_Json(rut)

        if vali_client == True:
            print(f"Ya existe el cliente con RUT {rut}, por lo tanto no se agregarán sus datos.")
        elif vali_client == False:

            

            sql = '''
                INSERT INTO cliente (rut, nombre, apellido, direccion, fono, correo, tipo, montoCredito, deuda)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            valores = (item['rut'], item['nombre'], item['apellido'], item['direccion'], item['fono'], item['correo'], item['tipo'], item['montoCredito'], item['deuda'])


            try:
                cursor.execute(sql, valores)
                conexion.commit()
                print("\n\n Datos Json traspasados con éxito...")
            except mysql.connector.Error as error:
                print(f"Error al insertar los datos: {error}")
                conexion.rollback()

