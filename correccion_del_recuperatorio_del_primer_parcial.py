from funciones import *

DEPOSITOS = ["Rosario", "cordoba", "salta", "bahia blanca"]
INSUMOS = ["Arduino UNO", "Sensor de temperatura", "Cable USB", "Display LCD", "Protoboard"]


    stock = [[0 for _ in range(len(INSUMOS))] for _ in range(len(DEPOSITOS))]

while True:
    print("Bienvenido al Sistema de Gestión de Insumos Tecnológicos para Escuelas Técnicas")
    print("1. Cargar stock de insumos")
    print("2. Ver depósitos con stock superior a 5000 unidades")
    print("3. Mostrar insumos con stock total superior a 3000 unidades")
    print("4. Identificar el depósito con mayor stock de insumos")
    print("5. Registrar ventas")
    print("6. Informe de ventas por depósito")
    print("7. Informe de ventas por insumo en cada depósito")
    print("8. Informe de reposición de stock")
    print("9. Porcentaje de stock de cada insumo respecto al total general")
    print("0. Salir")
    menu =int(input("Ingrese una opción: "))
    
    if menu == 1:
        stock = cargar_stock(INSUMOS, DEPOSITOS)
    elif menu == 2:
        mostrar_depositos(stock, INSUMOS, DEPOSITOS)
    elif menu == 3:
        mostrar_stock_total(stock, INSUMOS, DEPOSITOS)
    elif menu == 4:
        identificar_deposito_mayor_stock(stock, INSUMOS, DEPOSITOS)
    elif menu == 5:
        pass
    elif menu == 6:
        pass
    elif menu == 7:
        pass
    elif menu == 8:
        pass
    elif menu == 9:
        pass
    elif menu == 0:
        print("Saliendo...")
        break
    else:
        print("Por favor, ingrese una opción válida")
