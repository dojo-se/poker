# coding=utf8

# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def poker(jogador1, jogador2):
	dicCartas = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,
	"J":11, "Q":12, "K":13, "A":14}
	pontos1 = 0
	for carta in jogador1:
		pontos1 = dicCartas[carta[0]]

	pontos2 = 0
	for carta in jogador2:
		pontos2 = dicCartas[carta[0]]

	return pontos1 > pontos2 and 1 or 2


class PokerTest(unittest.TestCase):
    def test_carta_alta(self):
        self.assertEqual(1, poker(['5D','8C','9S','JS','AC'],
 								  ['2C','5C','7D','8S','QH']))

if __name__ == '__main__':
    unittest.main()