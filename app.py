from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebidas import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco Melancia', 5.0, 'Grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


def main():
    restaurante_praca.imprimir_cardapio

if __name__ == '__main__':
    main()
