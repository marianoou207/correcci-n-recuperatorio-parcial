def validar_entero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Error: ingrese solo números.")

def cargar_stock(INSUMOS:list, DEPOSITOS:list) -> int:
    print("Carga de stock")
    stock = [[0 for _ in range(len(INSUMOS))] for _ in range(len(DEPOSITOS))]
    for i in range(len(DEPOSITOS)):
        print(f"Depósito: {DEPOSITOS[i]}:")
        for j in range(len(INSUMOS)):
            cantidad = validar_entero(f"Ingrese la cantidad de {INSUMOS[j]}: ")
            stock[i][j] = cantidad
    print("Matriz de stock cargada:")
    mostrar_matriz(stock, INSUMOS, DEPOSITOS)
    return stock

def mostrar_matriz(matriz, INSUMOS, DEPOSITOS):
    print("Depósito\\insumos    ", *INSUMOS)
    for i in range(len(DEPOSITOS)):
        fila = DEPOSITOS[i] + "             "
        for j in range(len(INSUMOS)):
            fila += str(matriz[i][j]) + "           "
        print(fila)

def mostrar_depositos(stock:int,INSUMOS:list, DEPOSITOS:list, minimo=5000) -> str:
    print(f"Depósitos con stock total superior a {minimo} unidades:")
    for i in range(len(DEPOSITOS)):
        total = 0
        for j in range(len(INSUMOS)):
            total += stock[i][j]
        if total > minimo:
            print(f"El stock superior a {minimo} unidades en el depósito {DEPOSITOS[i]} es de: {total} unidades")

def mostrar_stock_total(stock:int,INSUMOS:list, DEPOSITOS:list, minimo=3000) -> str: 
    print(f"Insumos con stock total superior a {minimo} unidades:")
    for i in range(len(INSUMOS)):
        total = 0
        for j in range(len(DEPOSITOS)):
            total += stock[j][i]
        if total > minimo:
            print(f"El insumo {INSUMOS[i]} tiene un stock total de {total} unidades")

def identificar_deposito_mayor_stock(stock:int, INSUMOS:list, DEPOSITOS:list) -> str:
    print("Depósitos con mayor stock de insumos:")
    for j in range(len(INSUMOS)):
        maximo = stock[0][j]
        indice = 0
        for i in range(len(DEPOSITOS)):
            if stock[i][j] > maximo:
                maximo = stock[i][j]
                indice = i
        print(f"El depósito con mayor stock de {INSUMOS[j]} es {DEPOSITOS[indice]} con un máximo de {maximo} unidades")
