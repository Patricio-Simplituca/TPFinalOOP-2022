import csv

class Usuario():
    def __init__(self,nombre,user,password,tipo_usuario):
        self.nombre=nombre
        self.user=user
        self.password=password
        self.tipo_usuario=tipo_usuario

class Usuario_service():

    def login(self,user, password):
        with open('usuarios.csv',"r", newline='') as f:  
            reader = csv.DictReader(f)
            for row in reader:
                if row["user"] == user and row["password"]==password:
                    print("Ha ingresado con exito!")
                    persona_usuario = Usuario(
                        nombre=         row["nombre"],
                        user=           row["user"],
                        password=       row["password"],
                        tipo_usuario=   row["tipo_usuario"])
                    f.close()
                    return persona_usuario
            print("No se encuentra")
            f.close()
            return False

    def modificar_fechahora_entrada(self,numero_patente,fecha_a_modificar):
        with open('garage.csv',"r", newline='') as f:  
            reader = csv.DictReader(f,delimiter=",",fieldnames=["patente","fechahora_entrada","fechahora_salida"])
            registros_sin_campos=[row for i, row in enumerate(reader) if i != 0] 
        f.close()
        fechahora_entrada=input("Ingrese la nueva fecha/hora de entrada: ")
        for row in registros_sin_campos:
            if row["patente"]==numero_patente and row["fechahora_entrada"]==fecha_a_modificar :
                row["fechahora_entrada"]=fechahora_entrada
        with open('garage.csv', 'w', newline="") as f:
            writer=csv.DictWriter(f,delimiter=",",fieldnames=["patente","fechahora_entrada","fechahora_salida"])
            writer.writeheader()
            for row in registros_sin_campos:
                writer.writerow(row)
        f.close()
        print("Fecha y hora de entrada modificada con exito!")
        return False


    def modificar_fechahora_salida(self,numero_patente,fecha_a_modificar):
        with open('garage.csv',"r", newline='') as f:  
            reader = csv.DictReader(f,delimiter=",",fieldnames=["patente","fechahora_entrada","fechahora_salida"])
            registros_sin_campos=[row for i, row in enumerate(reader) if i != 0] 
        f.close()
        fechahora_salida=input("Ingrese la nueva fecha/hora de salida: ")
        for row in registros_sin_campos:
            if row["patente"]==numero_patente and row["fechahora_salida"]==fecha_a_modificar :
                row["fechahora_salida"]=fechahora_salida
        with open('garage.csv', 'w', newline="") as f:
            writer=csv.DictWriter(f,delimiter=",",fieldnames=["patente","fechahora_entrada","fechahora_salida"])
            writer.writeheader()
            for row in registros_sin_campos:
                writer.writerow(row)
        f.close()
        print("Fecha y hora de salida modificada con exito!")
        return False
