from datetime import datetime, timedelta

def calcular_horas_trabalhadas(entrada, saida, intervalo):
   try:
       if ":" not in entrada:
           if len(entrada) == 4:
               entrada = entrada[:2] + ":" + entrada[2:]
           else:
               raise ValueError("Formato de hora inválido. Use HH:mm ou HHmm.")

       if ":" not in saida:
           if len(saida) == 4:
               saida = saida[:2] + ":" + saida[2:]
           else:
               raise ValueError("Formato de hora inválido. Use HH:mm ou HHmm.")

       entrada_dt = datetime.strptime(entrada, '%H:%M')
       saida_dt = datetime.strptime(saida, '%H:%M')

       diferenca = saida_dt - entrada_dt

       if ":" not in intervalo:
           if len(intervalo) == 4:
               intervalo = intervalo[:2] + ":" + intervalo[2:]
           else:
               raise ValueError("Formato de hora inválido. Use HH:mm ou HHmm.")

       intervalo_dt = timedelta(hours=int(intervalo.split(":")[0]), minutes=int(intervalo.split(":")[1]))
       diferenca -= intervalo_dt

       horas, segundos = divmod(diferenca.seconds, 3600)
       minutos = segundos // 60

       return f"{horas} horas e {minutos} minutos"

   except ValueError as e:
       return str(e)

hora_entrada = input("Informe a hora de entrada (HH:mm ou HHmm): ")
hora_saida = input("Informe a hora de saída (HH:mm ou HHmm): ")
duracao_intervalo = input("Informe a duração do intervalo de almoço (HH:mm ou HHmm): ")

resultado = calcular_horas_trabalhadas(hora_entrada, hora_saida, duracao_intervalo)
print(f"Horas trabalhadas: {resultado}")
