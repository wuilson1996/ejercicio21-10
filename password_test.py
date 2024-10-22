password = "1234"
count_block = 3

while True:
    # validamos que los intentos no se hallan acabado.
    if count_block > 0:
        # ingresamos el password
        psw = input("Ingrese Password: ")
        # validamos que el password sea el correcto
        if psw == password:
            print("Password correcta")
            break# break se usa para detener el boocle
        else:
            #restamos 1 por cada intento incorrecto
            count_block -= 1 # esto es igual que decir count_block = count_block - 1
            print(f"Password incorrecta, le quedan {count_block} intentos")
    else:
        print("Cuenta bloqueada. Saliendo del while")
        break # break se usa para detener el boocle