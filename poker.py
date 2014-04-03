# coding=utf8

# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def poker(jogador1, jogador2):
    return 1

class PokerTest(unittest.TestCase):
    def test_carta_alta(self):
        self.assertEqual(1, poker(['5D','8C','9S','JS','AC'],
 								['2C','5C','7D','8S','QH']))

if __name__ == '__main__':
    unittest.main()