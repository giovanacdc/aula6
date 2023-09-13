import datetime
import unittest

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

class TestCalcularHorasTrabalhadas(unittest.TestCase):

    def test_calculo_horas_trabalhadas(self):
        entrada = "08:30"
        saida = "17:45"
        resultado = calcular_horas_trabalhadas(entrada, saida)
        self.assertEqual(resultado, "9 horas e 15 minutos")

    def test_formato_invalido(self):
        entrada = "08:30"
        saida = "1745"
        resultado = calcular_horas_trabalhadas(entrada, saida)
        self.assertEqual(resultado, "Formato de hora inválido. Use HH:MM.")

if __name__ == '__main__':
    unittest.main()
