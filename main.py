
import garagepy.usuario
import garagepy.menu

if __name__ == '__main__':
    persona_usuario=False
    while persona_usuario==False:
        print("\nBIENVENIDO AL GARAGE. POR FAVOR INICIE SESION.")
        user=input("Ingrese su usuario: ")
        password=input("Ingrese su contraseña: ")
        persona_usuario = garagepy.usuario.Usuario_service().login(user, password)
    while (garagepy.menu.menu(persona_usuario)==False and persona_usuario!=False):
        pass

    