from datetime import datetime

def calcular_segundos_transcurridos(hora):
    try:
        
        hora_actual = datetime.now().replace(microsecond=0)

       
        hora_ingresada = datetime.strptime(hora, "%H:%M:%S").replace(year=hora_actual.year, month=hora_actual.month, day=hora_actual.day)

        
        diferencia = hora_actual - hora_ingresada

        
        segundos_transcurridos = diferencia.total_seconds()

        if segundos_transcurridos < 0:
         
            segundos_transcurridos += 24 * 3600

        return int(segundos_transcurridos)
    except ValueError:
        return "Formato de hora incorrecto. Por favor, usa el formato HH:MM:SS."


hora_ingresada = input("Ingresa la hora en formato HH:MM:SS: ")


resultado = calcular_segundos_transcurridos(hora_ingresada)
print("Segundos transcurridos desde la hora ingresada:", resultado)

