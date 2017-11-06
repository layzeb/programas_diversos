# Programa que faz uma contagem regressiva para o aniversário de alguém
# A data do aniversário é estabelecida dentro da variável 'niver', no formato (AAAA/MM/DD)
# Desenvolvido em: 06 NOV 2017
# Autora: Layze Brandão
# Linguagem: Python 3.6.1


# -*- coding: utf8 -*-

from datetime import date

hoje = date.today()
niver = date(1992,11,11)


def balao():
    print('''
                 ,-""""-.
               ,'      _ `.
              /       )_)  \.
             :              :
             \              /
              \            /
               `.        ,'
                 `.    ,'
                   `.,'
                    /\`.   ,-._
                        `-'     ''')

def bolo():
    print('''
                           !     !     !
(          (    *         |V|   |V|   |V|        )   *   )       (
 )   *      )             | |   | |   | |        (       (   *    )
(          (           (*******************)    *       *    )    *
(     (    (           (    *         *    )               )    (
 )   * )    )          (   \|/       \|/   )         *    (      )
(     (     *          (<<<<<<<<<*>>>>>>>>>)               )    (
 )     )        ((*******************************))       (  *   )
(     (   *     ((      FELIZ ANIVERSÁRIO!!!!    ))      * )    (
 ) *   )        ((   *    *   *    *    *    *   ))   *   (      )
(     (         ((  \|/  \|/ \|/  \|/  \|/  \|/  ))        )    (
*)     )        ((^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^))       (      )
(     (   (**********************************************) )  * (''')


#verde = '\033[32m'
#vermelho = '\033[31m'
#clear = '\033[m'

if hoje.day < niver.day:
    print('\n\n')
    if niver.day - hoje.day == 1:
        print('Falta 1 dia para a data mais importante do ano!!!')
    else:
        print('Faltam {} dias para a data mais importante do ano!!!'.format(niver.day - hoje.day))
    #print('{}'.format(vermelho))
    balao()
elif hoje.day == niver.day:
    print('\n\n\n')
    print('-='*35)
    print('FELIZ ANIVERSÁRIO!!!!'.center(70))
    print('-='*35)
    #print('{}'.format(vermelho))
    bolo()

fim = input('\n\nPressione qualquer tecla para sair...')
