# Análisis de Ventas - TP OE

# Integrantes: Cabrera Mauricio
# Comision: 21

#Escenario elegido: Escenario B - Análisis de Ventas de una Pequeña Empresa

#El dataset utilizado fue creado en base a la siguientes fuente:
- https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6
  
# Este repositorio contiene el análisis de ventas para el trabajo práctico.
Estructura:
- /scripts: Código fuente
- /datos: Datasets utilizados
- /resultados: Gráficos e informes
  
# Descripción del Dataset Utilizado
Los datos se encuentran en `datos/ventas.csv`. Es un dataset simulado que contiene 200 registros de ventas. 
Las columnas que incluye son:
* "id": Identificador unico.
* "fecha": Fecha de la venta.
* "producto": Nombre de producto.
* "cantidad": Unidades vendidas.
* "precio": Precio unitario del producto.

## Revisión de Calidad (QA)
- Peer Review: Completado. Codigo validado.
- Seguridad: Se verificc la ausencia de datos sensibles y credenciales en el codigo.
- Revisado por: Luis (P3).

#  Instrucciones basicas para ejecutar el script
El proyecto está diseñado para ejecutarse en el entorno virtual de Google Colab. Para reproducir el análisis, siga estos pasos:

1. **Clonar el repositorio:**
   ```bash
   !git clone https://github.com/Mauus1/Analisis_de_ventas_TP
2. Ingresar al directorio del proyecto:
   ```bash
   %cd TU_REPO
4. Ejecutar el programa Una vez dentro de la carpeta:
   ```bash
   !python scripts/analisis_ventas.py
5. Resultados: Al ejecutar el script, la consola imprimira los totales calculados. Ademas, se generara de manera automatica un archivo llamado evolucion_ventas.txt dentro de la carpeta /resultados que contendrá el gráfico de la evolución mensual.
