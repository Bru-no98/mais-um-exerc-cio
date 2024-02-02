from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
#restaurante_mexicano = Restaurante ('Mexican Food', 'Mexicana')
#restaurante_japones = Restaurante('japa', 'Japones')

restaurante_praca.avaliar_restaurante('Bruno', 6)
restaurante_praca.avaliar_restaurante('lais', 1)
restaurante_praca.avaliar_restaurante('gui', 1)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
