import unittest
from stories import calcular_horas_trabalhadas

class TestCalcularHorasTrabalhadas(unittest.TestCase):

    def test_formato_valido_com_dois_pontos(self):
        entrada = "08:30"
        saida = "17:45"
        intervalo = "00:30"
        resultado = calcular_horas_trabalhadas(entrada, saida, intervalo)
        self.assertEqual(resultado, "8 horas e 45 minutos")

    def test_formato_valido_sem_dois_pontos(self):
        entrada = "0830"
        saida = "1745"
        intervalo = "0030"
        resultado = calcular_horas_trabalhadas(entrada, saida, intervalo)
        self.assertEqual(resultado, "8 horas e 45 minutos")

    def test_formato_invalido(self):
        entrada = "08:30"
        saida = "1745"
        intervalo = "00:30"
        resultado = calcular_horas_trabalhadas(entrada, saida, intervalo)
        self.assertEqual(resultado, "Formato de hora inválido. Use HH:mm ou HHmm.")

    def test_desconto_de_intervalo(self):
        entrada = "09:00"
        saida = "18:00"
        intervalo = "01:00"
        resultado = calcular_horas_trabalhadas(entrada, saida, intervalo)
        self.assertEqual(resultado, "8 horas e 0 minutos")

if __name__ == '__main__':
    unittest.main()
