import csv

# Diccionarios y variables nativas para almacenar nuestros datos
ventas_totales = 0
ventas_por_producto = {}
ventas_por_mes = {}

# 1. Cargar los datos usando la libreria estándar 'csv'
with open('datos/ventas.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        # Convertimos los textos del CSV a numeros
        cantidad = int(fila['cantidad'])
        precio = float(fila['precio'])
        ingreso = cantidad * precio
        producto = fila['producto']
        
        # Procesamos la fecha para extraer el mes
        fecha = fila['fecha']
        dia, mes, año = fecha.split('/')
        mes_año = f"{año}-{mes}" # Lo formateamos asi para que se ordene correctamente
        
        # --- CÁLCULOS DEL ESCENARIO B ---
        
        # A) Ventas totales
        ventas_totales += ingreso
        
        # B) Acumular cantidades para el producto mas vendido
        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad
            
        # C) Acumular ingresos para las ventas por mes
        if mes_año in ventas_por_mes:
            ventas_por_mes[mes_año] += ingreso
        else:
            ventas_por_mes[mes_año] = ingreso

# Buscar el producto con mayor cantidad vendida
producto_mas_vendido = ""
max_cantidad = 0
for prod, cant in ventas_por_producto.items():
    if cant > max_cantidad:
        max_cantidad = cant
        producto_mas_vendido = prod

# Imprimir resultados numéricos
print("--- RESULTADOS DEL ANÁLISIS ---")
print(f"Ventas Totales: ${ventas_totales}")
print(f"Producto más vendido: {producto_mas_vendido} ({max_cantidad} unidades)")
print("\nVentas por mes:")
for mes in sorted(ventas_por_mes.keys()):
    print(f"- {mes}: ${ventas_por_mes[mes]}")

# ------------- GRAFIFO -------------
print("\n--- GRÁFICO DE EVOLUCIÓN DE VENTAS ---")

# Guardamos el gráfico en la carpeta /resultados
with open('resultados/evolucion_ventas.txt', mode='w', encoding='utf-8') as archivo_resultado:
    archivo_resultado.write("Evolución de Ventas por Mes:\n\n")
    
    # Dibujamos barras usando el símbolo '#'. Cada '#' representa $100.
    for mes in sorted(ventas_por_mes.keys()):
        ingreso = ventas_por_mes[mes]
        barras = "#" * int(ingreso / 100)
        linea_grafico = f"{mes} | {barras} (${ingreso})"
        
        print(linea_grafico)
        archivo_resultado.write(linea_grafico + "\n")
        
print("\nGráfico de texto generado y guardado exitosamente en /resultados/evolucion_ventas.txt!")
