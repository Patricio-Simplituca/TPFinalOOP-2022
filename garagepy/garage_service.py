import csv
import datetime
from asyncio.windows_events import NULL

class Garage_service():

    def buscar_patente(self,numero_patente):
        with open('movil.csv',"r", newline='') as f: 
            reader = csv.DictReader(f)
            for row in reader:
                if row["patente"] ==numero_patente :
                    return row
            return None


    def registar_auto(self,auto_registro):
        registro={
        "patente":auto_registro.patente,
        "marca":auto_registro.marca,
        "modelo":auto_registro.modelo,
        "color":auto_registro.color,
        "observaciones":auto_registro.observaciones
        }
        with open("movil.csv", "a", newline="") as f:
            dict2=csv.DictWriter(f,delimiter=",",fieldnames=["patente","marca","modelo","color","observaciones"])
            dict2.writerow(registro)
        f.close()
        print("Auto registrado con exito!")
        return False


    def entrar(self,numero_patente):
        tiempo=datetime.datetime.now()
        ahora=tiempo.strftime('%d/%m/%Y %H:%M:%S')
        entrada={
        "patente":numero_patente,
        "fechahora_entrada":ahora,
        "fechahora_salida":NULL,
        }
        with open("garage.csv", "a", newline="") as f:
            dict2=csv.DictWriter(f,delimiter=",",fieldnames=["patente","fechahora_entrada","fechahora_salida"])
            dict2.writerow(entrada)
        f.close()
        print("El auto ha ingresado al garage con exito!")


    def sacar_auto(self,numero_patente):
        tiempo=datetime.datetime.now()
        ahora=tiempo.strftime('%d/%m/%Y %H:%M:%S')
        with open('garage.csv',"r", newline='') as f:  
            reader = csv.DictReader(f,delimiter=",",fieldnames=["patente","fechahora_entrada","fechahora_salida"])
            registros_sin_campos=[row for i, row in enumerate(reader) if i != 0] #son todos losregsitros menos los hjeaders- sacame los cmapos para tods los campos menos el que tenga indice 0 - asd es una varailbe/memoria en la puedo editar  
        f.close()
        for row in registros_sin_campos:
            if row["patente"]==numero_patente and row["fechahora_salida"]=="0":
                row["fechahora_salida"]=ahora
        with open('garage.csv', 'w', newline="") as f:
            writer=csv.DictWriter(f,delimiter=",",fieldnames=["patente","fechahora_entrada","fechahora_salida"])
            writer.writeheader()
            for row in registros_sin_campos:
                writer.writerow(row)
        f.close()
        print("Ha retirado el auto del garage con exito!")


    def comprobar_patente(self,numero_patente):
        with open('movil.csv',"r", newline='') as f: 
            reader = csv.DictReader(f)
            for row in reader:
                if row["patente"] ==numero_patente :
                    return not None
            return None


    def comprobar_auto_dentro_garage(self,numero_patente):
        with open('garage.csv',"r", newline='') as f: 
                reader = csv.DictReader(f)
                for row in reader:
                    if row["patente"] ==numero_patente and row["fechahora_salida"]=="0" :
                        return not None
                return None

    def ver_movimientos(self):
        print("\nMovimientos:\n")
        with open('garage.csv',"r", newline='') as f: 
                reader = csv.DictReader(f)
                for row in reader:
                    print(row)
        f.close()