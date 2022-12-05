import garagepy.garage_service
import garagepy.usuario
import garagepy.movil

def menu(persona_usuario):
    opcion=int(input("\n                 MENU\n \n1 - Buscar patente \n2 - Registrar patente  \n3 - Salir del Garage \n4 - Ingresar al garage \n5 - Modificar fecha y hora de entrada y salida \n6 - Ver movimientos \n7 - Salir\n \nElija una opcion: "))
    if opcion==1: #BUSCAR PATENTE
        patente=input("ingrese patente: ")
        auto=garagepy.garage_service.Garage_service().buscar_patente(patente)
        if auto is not None:
            print(auto)
            return False 
        elif auto is None:
            print("El auto no esta en la base de datos del garage. Registrelo en el menu.")
            return False 

    elif opcion==2: # REGISTRAR PATENTE
        patente=input("Ingrese patente a registrar: ")
        auto=garagepy.garage_service.Garage_service().comprobar_patente(patente)
        if auto is None:
            print("El auto no se encuentra en la base de datos del garage.Ingrese los datos del auto: ")
            patente=input("Ingrese numero de patente: ") 
            marca=input("Ingrese marca del auto: ") 
            modelo=input("Ingrese modelo del auto: ") 
            color=input("Ingrese color del auto: ") 
            observaciones=input("Ingrese alguna observacion del auto: ")
            auto_registro=garagepy.movil.Movil(patente,marca,modelo,color,observaciones)
            garagepy.garage_service.Garage_service().registar_auto(auto_registro)
        elif auto is not None:
            print("El auto ya se encuentra en la base de datos del garage.")
            return False 

    elif opcion==3:#SACAR AUTO DEL GARAGE
        patente=input("Ingrese patente del auto para retirarlo del garage: ")
        auto=garagepy.garage_service.Garage_service().comprobar_patente(patente)
        if auto is None:
            print("El auto no se encuentra registrado en la base de datos. Por favor registrelo primero. ")
            return False
        elif auto is not None:
            auto_en_garage=garagepy.garage_service.Garage_service().comprobar_auto_dentro_garage(patente)
            if auto_en_garage is None:
                print("El auto no esta en el garage")
                return False
            else:
                garagepy.garage_service.Garage_service().sacar_auto(patente)

    elif opcion==4:#INGRESAR AUTO AL GARAGE
        patente=input("Ingrese patente del auto para ingresarlo al garage: ")
        auto=garagepy.garage_service.Garage_service().comprobar_patente(patente)
        if auto is None:
            print("El auto no se encuentra registrado en la base de datos. Por favor registrelo primero. ")
            return False 
        elif auto is not None:
            auto_en_garage=garagepy.garage_service.Garage_service().comprobar_auto_dentro_garage(patente)
            
            if auto_en_garage is not None:
                print("El auto ya esta en el garage")
                return False 
            else:
                garagepy.garage_service.Garage_service().entrar(patente)

    elif opcion==5:#modificar fecha y hora de entrada y salida
        if persona_usuario.tipo_usuario=="ADMIN" :
            patente=input("Ingrese patente del auto: ")
            print("Si quiere modificar la fecha y hora de entrada escribra: 'ENTRADA'")
            print("Si quiere modificar la fecha y hora de salida escribra: 'SALIDA'")
            opcion_entrada_salida=input("Ingrese opcion: ")
            if opcion_entrada_salida=="ENTRADA":
                fecha_a_modificar=input("Ingrese la fecha de entrada que quiere modificar: ")
                confirmar=garagepy.garage_service.Garage_service().comprobar_fecha_entrada(fecha_a_modificar,patente)
                if confirmar is not None:
                    garagepy.usuario.Usuario_service().modificar_fechahora_entrada(patente,fecha_a_modificar)
                else:
                    print("No hay una fecha que coincida con su busqueda y/o la patente que ingreso, nunca ingreso al garage.")
                    return False
            elif opcion_entrada_salida=="SALIDA":
                fecha_a_modificar=input("Ingrese la fecha de salida que quiere modificar: ")
                confirmar=garagepy.garage_service.Garage_service().comprobar_fecha_salida(fecha_a_modificar,patente)
                if confirmar is not None:
                    garagepy.usuario.Usuario_service().modificar_fechahora_salida(patente,fecha_a_modificar)
                else:
                    print("No hay una fecha que coincida con su busqueda y/o la patente que ingreso, nunca ingreso al garage.")
                    return False
        elif persona_usuario.tipo_usuario=="USER":
            print("No tiene permisos para realizar esta accion")
            return False 
    elif opcion==6: #VER MOVIMIENTOS
        garagepy.garage_service.Garage_service().ver_movimientos()

    elif opcion==7:
        return True
    else:   
        print("Por favor ingrese una opcion correcta.")


    return False 