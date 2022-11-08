
import garagepy.usuario
import garagepy.menu

if __name__ == '__main__':
    print("BIENVENIDO AL GARAGE. POR FAVOR INICIE SESION")
    user=input("Ingrese su usuario: ")
    password=input("Ingrese su contraseña: ")
    persona_usuario = garagepy.usuario.Usuario_service().login(user, password)
    while (garagepy.menu.menu(persona_usuario)==False):
        pass

    