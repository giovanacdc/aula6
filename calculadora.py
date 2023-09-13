from datetime import datetime

def calcular_horas_trabalhadas(entrada, saida):
   try:
       entrada_dt = datetime.strptime(entrada, '%H:%M')
       saida_dt = datetime.strptime(saida, '%H:%M')

       diferenca = saida_dt - entrada_dt

       horas, segundos = divmod(diferenca.seconds, 3600)
       minutos = segundos // 60

       return f"{horas} horas e {minutos} minutos"

   except ValueError:
       return "Formato de hora inválido. Use HH:MM."

hora_entrada = input("Informe a hora de entrada (HH:MM): ")
hora_saida = input("Informe a hora de saída (HH:MM): ")

resultado = calcular_horas_trabalhadas(hora_entrada, hora_saida)
print(f"Horas trabalhadas: {resultado}")