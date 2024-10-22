from colorama import init, Fore, Back, Style
import requests
# Initialize Colorama
init()
def api_service():
    # Cambiarla por una consulta de api. consulta a base de datos.
    r = requests.get("http://localhost:8000/api/peliculas/")
    return r.json()

def api_service_update(puesto, status_puesto):
    payload = {
        "puesto": puesto,
        "status_puesto": status_puesto
    }
    r = requests.put("http://localhost:8000/api/peliculas/", data=payload)
    print(r.json())

def api_service_create():
    payload = {}
    r = requests.post("http://localhost:8000/api/peliculas/", data=payload)
    print(r.json())

def mostrar_peliculas(pls):
    print(Fore.WHITE+"--------- Peliculas disponibles -----------")
    for pelicula in pls:
        print(Fore.BLUE+"Pelicula: "+pelicula["titulo"])
        print(Fore.BLUE+"Cantidad de puestos disponible: "+str(pelicula["cont"]))
        #print("Puestos: "+str(pelicula["puestos"]))
        print(Fore.YELLOW+"------------------------------------------")
        for key, value in pelicula["puestos"].items():
            if value:
                print(Fore.GREEN+f"Puesto {key} esta {value}")
            else:
                print(Fore.RED+f"Puesto {key} esta {value}")
        print(Fore.YELLOW+"------------------------------------------")

def selected_option(pls, status_puesto=False, cont=1):#True,-1
    status = True
    while status:
        peli_select = input(Fore.WHITE+"Ingrese la pelicula requerida: ")
        peli_correct = False
        for pelicula in pls:
            if pelicula["titulo"] == peli_select:
                peli_correct = True
                if pelicula["cont"] > 0: # si es igual a cero mostramos que no tiene puestos disponibles.
                    while True:
                        puesto_select = input(Fore.WHITE+"Ingrese el puesto requerido: ")
                        if puesto_select in pelicula["puestos"].keys():# ["1", "2", "3"]
                            if pelicula["puestos"][puesto_select] != status_puesto: # True o False
                                api_service_update(puesto_select, status_puesto)
                                status = False
                                if status_puesto == False:
                                    print(Fore.GREEN+f"Ticket comprado correctamente. {peli_select} en puesto: {puesto_select}")
                                else:
                                    print(Fore.GREEN+f"Ticket devuelto correctamente. {peli_select} en puesto: {puesto_select}")
                                break
                            else:
                                if status_puesto == False:
                                    print(Fore.RED+"Puesto ya esta ocupado")
                                else:
                                    print(Fore.RED+"Puesto no esta ocupado, no se puede devolver")
                else:
                    print(Fore.RED+"Esta pelicula no tiene puestos disponibles")
            if peli_correct:
                break
        if not peli_correct:
            print(Fore.RED+"Verifique que el nombre de la pelicula sea el correcto")

def main():
    peliculas = api_service()
    while True:
        print(Fore.WHITE+"Opcion 1 Venta de ticket.\nOpcion 2 Devolucion de ticket.\nOpcion 3 peliculas disponibles.\nOpcion 4 agregar peliculas.\nOpcion 0 Salir.")
        option = input(Fore.WHITE+"Ingrese una opcion: ")
        # salimos del programa.
        if option == "0":
            print(Fore.WHITE+"Saliendo del programa")
            break
        # venta de tickets.
        elif option == "1": # else if:
            #mostrar_peliculas(peliculas)
            selected_option(peliculas)
            peliculas = api_service()
        # devolucion de tickets.
        elif option == "2":
            #mostrar_peliculas(peliculas)
            selected_option(peliculas, True, -1)
            peliculas = api_service()
        elif option == "3":
            mostrar_peliculas(peliculas)
        elif option == "4":
            api_service_create()
            peliculas = api_service()

    print(Fore.GREEN+"Ha finalizado el programa")

if __name__ == "__main__":
    api_service_update("Marvel1", "1", False, 1)