# coding=utf8

# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

dicCartas = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,
	"J":11, "Q":12, "K":13, "A":14}

def poker(mao1, mao2):
	ganhador = 0

	mao1.sort();
	mao2.sort();

	trinca1 = temTrinca(mao1)
	trinca2 = temTrinca(mao2)
	if trinca1 and not trinca2:
		ganhador = 1
	elif trinca2 and not trinca1:
		ganhador = 2
	elif trinca1 > trinca2:
		ganhador = 1
	else:
		ganhador = 2


	return ganhador

#def poker2(mao1, jogador2):

def cartaAlta(mao1, mao2):
	pontos1 = 0
	#carta alta
	for carta in mao1:
		if getValor(carta) > pontos1:
			pontos1 = getValor(carta)

	pontos2 = 0
	for carta in mao2:
		if getValor(carta) > pontos2:
			pontos2 = getValor(carta)

	return pontos1 > pontos2 and 1 or 2

def temPar(mao):
	for carta1 in mao:
		for carta2 in mao:
			if getValor(carta1) == getValor(carta2) and carta1 != carta2:
				return True

	return False

def temTrinca(mao):
	valor = getValor(mao[0])
	conta = 1
	for carta in mao[1:]:
		novoValor = getValor(carta)
		if valor == novoValor:
			conta += 1
			if conta == 3:
				return True
		else:
			valor = novoValor
			conta = 1
	return False

def doisPares(mao):
	pass


def getValor(carta):
	return dicCartas[carta[0]]

class PokerTest(unittest.TestCase):
	def test_carta_alta_1(self):
		self.assertEqual(1, cartaAlta(	['5D','8C','9S','JS','AC'],
									['2C','5C','7D','8S','QH']))

	def test_carta_alta_2(self):
		self.assertEqual(2, cartaAlta(	['5D','8C','9S','JS','QC'],
									['AC','5C','7D','8S','8H']))

	def test_carta_alta_3(self):
		self.assertEqual(1, cartaAlta(	['5D','TC','9S','2S','9C'],
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