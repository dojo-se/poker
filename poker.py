# coding=utf8

# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

dicCartas = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,
	"J":11, "Q":12, "K":13, "A":14}

def poker(jogador1, jogador2):
	pontos1 = 0
	#carta alta
	for carta in jogador1:
		if getCarta(carta) > pontos1:
			pontos1 = getCarta(carta)

	pontos2 = 0
	for carta in jogador2:
		if getCarta(carta) > pontos2:
			pontos2 = getCarta(carta)

	return pontos1 > pontos2 and 1 or 2

#def poker2(jogador1, jogador2):


def temPar(mao):
	for carta1 in mao:
		for carta2 in mao:
			if getCarta(carta1) == getCarta(carta2) and carta1 != carta2:
				return True

	return False
def temTrinca(mao):
	for carta1 in mao:
		for carta2 in mao:
			for carta3 in mao:
				if getCarta(carta1) == getCarta(carta2) and \
					getCarta(carta2) == getCarta(carta3) and \
					carta1 != carta2 and carta1 != carta3 and carta2 != carta3:
					return True

	return False

def getCarta(carta):
	return dicCartas[carta[0]]

class PokerTest(unittest.TestCase):
	def test_carta_alta_1(self):
		self.assertEqual(1, poker(	['5D','8C','9S','JS','AC'],
									['2C','5C','7D','8S','QH']))

	def test_carta_alta_2(self):
		self.assertEqual(2, poker(	['5D','8C','9S','JS','QC'],
									['AC','5C','7D','8S','8H']))

	def test_carta_alta_3(self):
		self.assertEqual(1, poker(	['5D','TC','9S','2S','9C'],
									['2C','5C','7D','8S','8H']))

	def test_um_par(self):
		self.assertEqual(True, temPar(['8D','QC','7S','JS','8C']))

	def test_nao_tem_um_par(self):
		self.assertEqual(False, temPar(['5D','8C','9S','JS','AC']))

	def test_uma_trinca(self):
		self.assertEqual(True, temPar(['8D','QC','8S','JS','8C']))

	def test_nao_tem_uma_trinca(self):
		self.assertEqual(False, temPar(['5D','8C','9S','JS','AC']))


if __name__ == '__main__':
    unittest.main()