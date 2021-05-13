# PyRestaurant

billetes = (5, 10, 20, 50, 100, 200, 500)
total_comanda = 0

# creamos dos listas una para platos y otra para precios
platos = ["Ensalada de habichuelas", "Lasaña vegetal", "Albondigas de soja", "Salteado de tofu y esparragos", "Croquetas de quinoa", "Hamburguesas de seitan", "Curry de verduras", "Berenjenas y pimientos rellenos", "Nuggets de garbanzos", "Pisto vegetal", "Sopa de maimones"]
precios = [5, 7, 8, 8, 10, 12, 10, 10, 8, 8, 7]

# combinamos las dos listas en un diccionario
menu = dict(zip(platos,precios))

saludo_camarero = 'Buenas tardes, familia. \nFuera de carta dejenme recomendarle: \n'

def cantar_carta():
    print("===========================")
    print(saludo_camarero)
    index = 0
    for plato, precio in menu.items():
        index = int(index + 1)
        print(str(index) + ' ☛ ' + plato )
    print("¿Que van a querer comer?")
    pedido()

def pedido():
    comanda = []
    total_comanda = 0
    seguir_pidiendo = True
    while seguir_pidiendo == True:
        plato = input().capitalize() #usamos capitalize para poder poner el plato en mays o min indistintamente
        if (plato == 'Nada mas'):
            seguir_pidiendo = False
        elif (plato in menu):
            comanda.append(plato) # Añadimos plato a la comanda
            precio_plato = int(menu.get(plato)) # Obtenemos el precio del plato del dict
            total_comanda = total_comanda + precio_plato # Sumamos precio del plato a la comanda
            print("Muy bien: " + plato + " (" + str(precio_plato) + "€). ¿Algo mas?")
            seguir_pidiendo = True
        else:
            print("Lo siento. No tenemos ese plato en carta ¿Querria alguna otra cosa?")
            seguir_pidiendo = True

    print("*************************\n¡Estupendo! Le repito la comanda:\n")
    for plato in comanda:
        print('☛ ' + str(plato))
    print("Serian en total " + str(total_comanda) + " euros. ¿Van a necesitar cambio? [Y/n]")
    need_cambio = input()
    if need_cambio:
        print("Ok. ¿De cuanto?")
        for billete in billetes:
            if billete > total_comanda:
                print(billete)
        billetecambio = int(input())
        vuelta = billetecambio - total_comanda
        print("Genial. Le devuelvo " + str(vuelta) + "€")
        print("¡Muchas gracias!")
    else:
        print("Genial. Muchas gracias.")

cantar_carta()