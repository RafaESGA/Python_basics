def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿cuántos pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

menu = '''
Bienvenido al conversor de monedas 💰

1 -> Pesos mexicanos
2 -> Pesos colombianos
3 -> Pesos argentinos

Elige una opción: '''

opcion = input(menu)

if opcion == '1':
    conversor("mexicanos", 21.3)
elif opcion == '2':
    conversor("colombianos", 3850.25)
elif opcion == '3':
    conversor("argentinos", 77.47)
else:
    print('Ingresa una opción correcta por favor')

