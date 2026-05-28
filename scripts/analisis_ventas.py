import csv

# Se utilizan diccionarios nativos en lugar de listas para optimizar la busqueda 
# y agrupación de datos en memoria, evitando el uso de dependencias externas pesadas.
ventas_totales = 0
ventas_por_producto = {}
ventas_por_mes = {}

# Se emplea 'with open' para asegurar que el archivo se cierre automáticamente tras la lectura, 
# previniendo fugas de memoria o bloqueos del archivo de datos.
with open('datos/ventas.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        # Es necesario realizar un casting (int y float) porque DictReader extrae 
        # todos los datos como cadenas de texto, impidiendo operaciones matematicas.
        cantidad = int(fila['cantidad'])
        precio = float(fila['precio'])
        ingreso = cantidad * precio
        producto = fila['producto']
        
        # Se formatea la fecha como YYYY-MM para garantizar que, al ordenar el diccionario 
        # más adelante, el ordenamiento alfabético coincida exactamente con el orden cronológico.
        fecha = fila['fecha']
        dia, mes, año = fecha.split('/')
        mes_año = f"{año}-{mes}" 
        
        #Guardamos las ventas totales
        ventas_totales += ingreso
        
        # Se verifica si la clave existe para inicializarla o sumar al acumulado, 
        # implementando así una lógica de agrupacion eficiente.
        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad
            
        # Acumulamos ingresos para las ventas por mes
        if mes_año in ventas_por_mes:
            ventas_por_mes[mes_año] += ingreso
        else:
            ventas_por_mes[mes_año] = ingreso

# Se itera sobre los items del diccionario para determinar el máximo de forma secuencial, 
# manteniendo una complejidad algoritmica lineal.
producto_mas_vendido = ""
max_cantidad = 0
for prod, cant in ventas_por_producto.items():
    if cant > max_cantidad:
        max_cantidad = cant
        producto_mas_vendido = prod

# Imprimir resultados numéricos
print("--- RESULTADOS DEL ANALISIS ---")
print(f"Ventas Totales: ${ventas_totales}")
print(f"Producto mas vendido: {producto_mas_vendido} ({max_cantidad} unidades)")
print("\nVentas por mes:")
for mes in sorted(ventas_por_mes.keys()):
    print(f"- {mes}: ${ventas_por_mes[mes]}")

# ------------- GRAFICO SIMPLE --------------
print("\n--- GRAFICO DE EVOLUCION DE VENTAS ---")

# Usamos una ruta corta ('resultados/...') en lugar de poner la dirección exacta de mi PC. 
# El motivo de esto es evitar que el programa tire error cuando otra persona 
# descargue nuestro proyecto y quiera hacer funcionar el código en su propia máquina.
with open('resultados/evolucion_ventas.txt', mode='w', encoding='utf-8') as archivo_resultado:
    archivo_resultado.write("Evolucion de Ventas por Mes:\n\n")
    

    for mes in sorted(ventas_por_mes.keys()):
        ingreso = ventas_por_mes[mes]
        # Se divide el ingreso por 100 para crear una escala visual proporcional 
        # y evitar que la impresión de barras (símbolo '#') desborde la pantalla.
        barras = "#" * int(ingreso / 100)
        linea_grafico = f"{mes} | {barras} (${ingreso})"
        
        print(linea_grafico)
        archivo_resultado.write(linea_grafico + "\n")
        
print("\nGrafico de texto generado y guardado exitosamente en /resultados/evolucion_ventas.txt!")
