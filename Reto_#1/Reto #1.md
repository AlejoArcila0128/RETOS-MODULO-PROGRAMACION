<div align="center">
  
# 🚀Reto #1 programación🚀

**Alejandro Arcila Rua**

</div>

## Sistema de monitoreo de vuelo para un cohete suborbital

A continuación se extiende un documento recopilatorio de los diferentes apartados relacionados con el reto #1 de programación, el cual trata acerca de un cohete y su sistema de monitoreo de vuelo.

## Análisis E/P/S

### Entrada

| Elemento | Descripción | Tipo | Unidad |
| --- | --- | --- | --- |
| Presion | Presión atmosférica | float | Hpa |
| Aceleracion | Aceleración del cohete | float | M/s^2 |
| Temperatura | Temperatura del cohete | float | C° |

### Procesos

| Elemento | Descripción | Retorna |
| --- | --- | --- |
| Calculo_Altitud | Fórmula barométrica proporcionada | Altitud |
| Determinar_estado_vuelo | Comparación entre altitud actual vs altitud previa (3 posibles estados) | 1, 2, 3 |
| evaluar_alerta_temperatura | Emisión de alerta si sobrepasa límite | temp_celsius > Límite crítico |
| texto_estado | Transforma el return de "determinar_estado_vuelo" de un número en un estado real | "Ascenso" / "Apogeo / Caída libre" / "Despliegue de paracaídas" |

### Salida

| Elemento | Descripción | Tipo |
| --- | --- | --- |
| altitud_maxima | Altitud máxima alcanzada en el vuelo | float |
| promedio_temp | Promedio de temperatura de todo el vuelo | float |
| aceleracion_maxima | Aceleración máxima alcanzada | float |
| t | Momento del vuelo | int |

Como parte de los entregables, a continuación se enlista el pseudocódigo correspondiente a las funciones usadas en el código "main".

> El siguiente formato está proporcionado mediante el uso de la herramienta extensión Code blocks de Google Workspace; no corresponde a imágenes ni uso de IA.

## Funciones

### #1 — Cálculo de altitud

La siguiente función tiene como objetivo agrupar el cálculo de la altitud en la que se encuentre el cohete en función del valor otorgado por la posterior toma de presión mediante la fórmula barométrica.

```python
# Inicio funcion
def calcular_altitud(presion_hpa: float) -> float:
    p0 = 1013.25
    return 44330 * (1 - (presion_hpa / p0) ** 0.1903)
# Fin función
```

### #2 — Determinar estado de vuelo

La siguiente función busca establecer los diferentes estados de vuelo como valores numéricos, para posteriormente en otra función hacer uso de esas nuevas "etiquetas" y así simplificar mejor el código.

```python
# Inicio función
def determinar_estado_vuelo(altitud_actual: float, altitud_previa: float, aceleracion: float) -> int:
    if altitud_actual > altitud_previa:
        return 1  # Ascenso
    elif aceleracion <= -9.0:
        return 2  # Apogeo / Caída libre
    else:
        return 3  # Despliegue de paracaídas
# Fin función
```

### #3 — Evaluar alerta de temperatura

Esta función busca establecer el límite crítico para que se despliegue la alerta de temperatura y luego usarla en el "main".

```python
# Inicio Función
def evaluar_alerta_temperatura(temp_celsius: float) -> bool:
    LIMITE_CRITICO = 65.0
    return temp_celsius > LIMITE_CRITICO
# Fin función
```

### #4 — Texto del estado

Mediante el uso de la función #2 y esta, es posible hacer un uso del código más eficiente gracias a que ahora al evaluar.

```python
def texto_estado(codigo: int) -> str:
    if codigo == 1:
        return "Ascenso"
    elif codigo == 2:
        return "Apogeo / Caída libre"
    else:
        return "Despliegue de Paracaídas"
```

### #5 — Lectura de datos simulados

Esta función sirve como los generadores de datos correspondientes para que todo el código "main" funcione.

```python
def leer_datos_simulados(t: int) -> tuple:
    import random
    presion = random.uniform(700.0, 1300.25)      # Simula presión en hPa
    aceleracion = random.uniform(-10.0, 30.0)     # Simula aceleración en m/s^2
    temperatura = random.uniform(-40.0, 80.0)     # Simula temperatura en °C
    return presion, aceleracion, temperatura
```

## Diagrama de flujo

El siguiente diagrama de flujo tiene como objetivo facilitar el planteamiento previo del código en Python, establecido un orden claro de como se ejecutara este mismo.

![imagen](Reto_#1/Diagrama_Flujo/Diagrama_flujo_Reto.png)
