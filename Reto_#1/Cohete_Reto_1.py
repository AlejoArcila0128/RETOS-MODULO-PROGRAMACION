#RETO PROGRAMACIÓN 1 - COHETE SUBORBITAL - ALEJANDRO ARCILA RUA

def calcular_altitud(presion_hpa: float) -> float:
    p0 = 1013.25  # Presión a nivel del mar en hPa
    return 44330 * (1 - (presion_hpa / p0) ** 0.1903)

#EL USO DE LA FLECHITA PARA QUE LA FUNCION RETORNE UN TIPO DE DATO FUE CONSULTADO MEDIANTE IA

def determinar_estado_vuelo(altitud_actual: float, altitud_previa: float, aceleracion: float) -> int:
    if altitud_actual > altitud_previa:
        return 1  # Ascenso
    elif aceleracion <= -9.0:
        return 2  # Apogeo / Caída libre
    else:
        return 3  # Despliegue de paracaídas


def evaluar_alerta_temperatura(temp_celsius: float) -> bool:
    LIMITE_CRITICO = 65.0
    return temp_celsius > LIMITE_CRITICO


def texto_estado(codigo: int) -> str:
    if codigo == 1:
        return "Ascenso"
    elif codigo == 2:
        return "Apogeo / Caída libre"
    else:
        return "Despliegue de Paracaídas"


def leer_datos_simulados(t: int) -> tuple:
    import random
    presion = random.uniform(700.0, 1300.25)  # Simula presión en hPa
    aceleracion = random.uniform(-10.0, 30.0)  # Simula aceleración en m/s^2
    temperatura = random.uniform(-40.0, 80.0)  # Simula temperatura en °C
    return presion, aceleracion, temperatura

def main():
    altitud_previa = 0.0
    altitud_maxima = 0.0
    apogeo_detectado = False
    suma_temp = 0.0
    contador = 0
    aceleracion_maxima = float("-inf")
    t = 0

#El ":.2f" Se investigo para limitar que el numero unicamente arroje 2 decimales

    while True:
        presion, aceleracion, temperatura = leer_datos_simulados(t)
        altitud_actual = calcular_altitud(presion)

        if altitud_actual > altitud_maxima:
            altitud_maxima = altitud_actual

        if (not apogeo_detectado) and (altitud_actual < altitud_previa):
            apogeo_detectado = True
            print(f">> Apogeo detectado cerca de t={t-1} (altitud máx: {altitud_maxima:.2f} m)")

        estado = determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)
        alarma = evaluar_alerta_temperatura(temperatura)

        suma_temp += temperatura
        contador += 1
        if aceleracion > aceleracion_maxima:
            aceleracion_maxima = aceleracion

        print(f"t = {t} s | altitud = {altitud_actual:.2f} m | estado = {texto_estado(estado)} "
              f"| alarma_temp = {'SI' if alarma else 'no'}")

        altitud_previa = altitud_actual
        t += 1

        if altitud_actual <= 0 and t > 1:
            print("\n*** ATERRIZAJE DETECTADO ***")
            break

    promedio_temp = suma_temp / contador if contador > 0 else 0.0
    print("\n--- RESUMEN DE VUELO ---")
    print(f"Apogeo máximo alcanzado: {altitud_maxima:.2f} m")
    print(f"Temperatura promedio: {promedio_temp:.2f} °C")
    print(f"Aceleración máxima registrada: {aceleracion_maxima:.2f} m/s^2")
    print(f"Duración total: {t} s")

if __name__ == "__main__":
    main()

